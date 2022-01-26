const UserService = require("../services/user.service");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");
const {RefreshToken} = require("../models/index");

const {validateEmail, validatePassword} = require("../validations/auth.validation");
const {v4: uuidv4} = require("uuid");
const {sendVerifyMail} = require("../services/email.service");

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

        sendVerifyMail(email, unique);

        user.token = jwt.sign({
            id: user.id,
            email: user.email,
            username: user.username
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
            
            // if(user[0].verified === false){
            //     return res.status(400).json({
            //         success: false,
            //         message: 'Please verify your email'
            //     });
            // }

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
                        email: user[0].email,
                        username: user[0].username
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

    console.log(requestToken);
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
                email: user.email,
                username: user.username
            }, process.env.TOkEN_KEY, {
                expiresIn: process.env.JWT_EXPIRATION_TIME
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
    const {verifyString} = req.body;

    if(!verifyString){
        return res.status(400).json({
            success: false,
            message: 'verify string is required'
        });
    }

    const userService = new UserService();
    userService.getUserByVerifyString(verifyString).then(user => {
        if(!user){
            return res.status(400).json({
                success: false,
                message: 'verify string is invalid'
            });
        }
        if(user.verified){
            return res.status(400).json({
                success: false,
                message: 'user is already verified'
            });
        }
        user.verified = true;
        user.verifyString = null;
        user.save().then(() => {
            return res.status(200).json({
                success: true,
                message: 'user is verified'
            });
        });
    }).catch(err => {
        console.log(err);
        return res.status(500).json({
            success: false,
            message: err.message
        });
    });

}





module.exports = {
    login,
    register,
    refreshToken,
    verify
};
