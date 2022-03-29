const UserService = require("../services/user.service");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");
const {RefreshToken} = require("../models/index");
const {validateEmail, validatePassword} = require("../validations/auth.validation");
const {v4: uuidv4} = require("uuid");
const EmailService = require("../services/email.service");


const register = async (req, res) => {
    let userService;
    try {
        const { email, password } = req.body;
        if(!email || !password){
            return res.status(400).json({
                success: false,
                message: 'Please enter all fields'
            });
        }

        if(!validateEmail(email)){
            return res.status(400).json({
                success: false,
                message: 'Please enter a valid email'
            });
        }

        if(!validatePassword(password)){
            return res.status(400).json({
                success: false,
                message: 'Please enter a valid password'
            });
        }

        userService = new UserService();

        const testIfEmailExists = await userService.getUserByEmail(email);
        console.log(testIfEmailExists.length);
        if(testIfEmailExists.length > 0){
            return res.status(400).json({
                success: false,
                message: 'Email already exists'
            });
        }

        let encryptedPassword = await bcrypt.hash(password, 10);

        let unique = uuidv4();

        const user = await userService.createUser({
            email: email.toLowerCase(),
            password: encryptedPassword,
            verifyString: unique
        });
        
        EmailService.sendVerifyMail(email, unique);

        user.token = jwt.sign({
            id: user.id,
            email: user.email
        }, process.env.TOKEN_KEY, {
            expiresIn: parseInt(process.env.JWT_EXPIRATION_TIME)
        });

        return res.status(200).json({
            success: true,
            message: 'User created',
            token: user.token
        });

    } catch (err) {
        console.log(err);
        return res.status(500).json({
            success: false,
            message: err.message
        });
    }

};

const login = (req, res) => {
    const { email, password } = req.body;
    if(!email || !password){
        return res.status(400).json({
            success: false,
            message: 'Please enter all fields'
        });
    }

    const userService = new UserService();
    userService.getUserByEmail(email)
        .then(user => {
            if(user.length === 0){
                return res.status(400).json({
                    success: false,
                    message: 'User not found'
                });
            }
            
            if(user[0].verified === false){
                return res.status(400).json({
                    success: false,
                    message: 'Please verify your email'
                });
            }

            bcrypt.compare(password, user[0].password)
                .then(async isMatch => {
                    if (!isMatch) {
                        return res.status(400).json({
                            success: false,
                            message: 'Incorrect password'
                        });
                    }


                    user[0].token = jwt.sign({
                        id: user[0].id,
                        email: user[0].email
                    }, process.env.TOKEN_KEY, {
                        expiresIn: parseInt(process.env.JWT_EXPIRATION_TIME)
                    });

                    let refreshToken = await RefreshToken.createToken(user[0]);

                    return res.status(200).json({
                        success: true,
                        message: 'User logged in',
                        token: user[0].token,
                        refreshToken: refreshToken
                    });
                })
                .catch(err => {
                    console.log(err);
                    return res.status(500).json({
                        success: false,
                        message: err.message
                    });
                });
        })
        .catch(err => {
            console.log(err);
            return res.status(500).json({
                success: false,
                message: err.message
            });
        });
};

const refreshToken = (req, res) => {
    const { refreshToken: requestToken } = req.body;
    if(requestToken === null){
        return res.status(400).json({
            success: false,
            message: 'refresh token is required'
        });                            
    }
    // console.log(requestToken);
    RefreshToken.findOne({
        where: {
            token: requestToken
        }
    })
        .then(async token => {
            if(!token){
                return res.status(400).json({
                    success: false,
                    message: 'refresh token is invalid'
                });
            }
            if(RefreshToken.verifyExpiration(token)){
                RefreshToken.destroy({
                    where: {
                        token: requestToken
                    }
                });
                return res.status(403).json({
                    success: false,
                    message: 'refresh token has expired. Please login again'
                });
            }
            const user = await token.getUser();
            let newAccessToken = jwt.sign({
                id: user.id,
                email: user.email
            }, process.env.TOKEN_KEY, {
                expiresIn: parseInt(process.env.JWT_EXPIRATION_TIME)
            });
            return res.status(200).json({
                success: true,
                message: 'refresh token is valid',
                accessToken: newAccessToken,
                refreshToken: requestToken
            });
        })
        .catch(err => {
            console.log(err);
            return res.status(500).json({
                success: false,
                message: err.message
            });
        });
};

const verify = (req, res) =>  {
    const {verifyString} = req.params;

    if(!verifyString){
        return res.status(400).render('pages/verifyEmail', {
            success: false,
            message: 'verification string is required'
        });
    }

    const userService = new UserService();
    userService.getUserByVerifyString(verifyString).then(users => {
        let user = users[0];
        console.log(user)
        if(!user){
            return res.status(400).render('pages/verifyEmail', {
                success: false,
                message: 'verify string is invalid'
            });
        }
        if(user.verified){
            return res.status(400).render('pages/verifyEmail', {
                success: false,
                message: 'user has already been verified'
            });
        }
        user.verified = true;
        user.verifyString = null;
        user.save().then(() => {
            return res.status(200).render('pages/verifyEmail', {
                success: true,
                message: 'user has been verified'
            });
        });
    }).catch(err => {
        console.log(err);
        return res.status(500).render('pages/verifyEmail', {
            success: false,
            message: err.message
        });
    });
}

const resetPasswordEmail = (req, res) => {
    const {email} = req.body;

    if (!email) {
        return res.status(400).json({
            success: false,
            message: 'Email is required'
        });
    }


    let userService = new UserService();
    userService.getUserByEmail(email).then(users => {
        let user = users[0];
        if (!user) {
            return res.status(400).json({
                success: false,
                message: 'Email is invalid'
            });
        }
        if (!user.verified) {
            return res.status(400).json({
                success: false,
                message: 'User is not verified'
            });
        }
        user.resetPasswordToken = uuidv4();
        let today = new Date();
        user.resetPasswordExpire = today.setSeconds(today.getSeconds() + process.env.EXPIRE_TIME)
        user.save().then(() => {
            EmailService.sendResetPasswordMail(user.email, user.resetPasswordToken);
            return res.status(200).json({
                success: true,
                message: 'Reset password email is sent'
            });
        }).catch(err => {
            return res.status(500).json({
                success: false,
                message: err
            });
        })
    });

}

const resetPassword = (req, res) => {
    console.log(req.body);
    console.log(req.params);

    const {token, password, confirmPassword} = req.body;

    if (!token) {
        return res.status(400).render('pages/changePassword' ,{
            success: false,
            title: 'Reset Password Page',
            token: token,
            messages: {
                error: 'reset password token is required'
            }
        });
    }

    if (!password) {
        return res.status(400).render('pages/changePassword', {
            success: false,
            title: 'Reset Password Page',
            token: token,
            messages: {
                error: 'password is required'
            }
        });
    }

    if(!confirmPassword){
        return res.status(400).render('pages/changePassword', {
            success: false,
            title: 'Reset Password Page',
            token: token,
            messages: {
                error: 'confirm password is required'
            }
        });
    }

    if(password !== confirmPassword){
        return res.status(400).render('pages/changePassword', {
            success: false,
            title: 'Reset Password Page',
            token: token,
            messages: {
                error: 'Password and confirm password must be same'
            }
        });
    }

    if(!validatePassword(password)){
        return res.status(400).render('pages/changePassword', {
            success: false,
            title: 'Reset Password Page',
            token: token,
            messages: {
                error: 'Password must be at least 8 characters long, contain at least one number and one uppercase and lowercase letter, and one special character'
            }
        });
    }



    let userService = new UserService();
    userService.getUserByResetPasswordToken(token).then(async users => {
        let user = users[0];
        if (!user) {
            return res.status(400).render('pages/changePassword', {
                success: false,
                title: 'Reset Password Page',
                token: token,
                messages: {
                    error: 'reset password token is invalid'
                }
            });
        }

        if (!user.verified) {

            return res.status(400).render('pages/changePassword', {
                success: false,
                title: 'Reset Password Page',
                token: token,
                messages: {
                    error: 'user has not validate his mail'
                }
            })
        }

        if (user.resetPasswordExpire < new Date()) {
            return res.status(400).render('pages/changePassword', {
                success: false,
                title: 'Reset Password Page',
                token: token,
                messages: {
                    error: 'reset password token is expired'
                }
            })
        }


        user.password = await bcrypt.hash(password, 10);
        user.resetPasswordToken = null;
        user.resetPasswordExpire = null;
        user.save().then(() => {
            return res.status(200).render('pages/changePassword', {
                success: true,
                title: 'Reset Password Page',
                token: token,
                messages: {
                    success: 'Password has changed'
                }
            })
        }).catch(err => {
            return res.status(500).render('pages/changePassword', {
                success: false,
                title: 'Reset Password Page',
                token: token,
                messages: {
                    error: err
                }
            })
        })
    }).catch(err => {
        return res.status(500).render('pages/changePassword', {
            success: false,
            title: 'Reset Password Page',
            token: token,
            messages: {
                error: err
            }
        })
    });
}

const resetPasswordPage = (req, res) => {
    const {token} = req.query;

    if(!token){
        return res.status(400).render('pages/changePassword', {
            title: 'Reset Password Page',
            token: token,
            messages: {
                error: 'token is required'
            }
        })
    }

    return res.status(200).render('pages/changePassword',  {
        title: 'Reset Password Page',
        token: token,
        messages: {
        }
    })
}

module.exports = {
    register,
    login,
    refreshToken,
    verify,
    resetPasswordEmail,
    resetPassword,
    resetPasswordPage
}