const {validatePassword} = require("../validations/auth.validation");
const UserService = require("../services/user.service");
const bcrypt = require("bcryptjs");

const changePassword = (req, res) => {
    const {oldPassword, newPassword} = req.body;
    if (oldPassword === null || newPassword === null) {
        return res.status(400).json({
            success: false,
            message: 'Please enter all fields'
        });
    }

    if(!validatePassword(newPassword)){
        return res.status(400).json({
            success: false,
            message: 'Please enter a valid password'
        });
    }

    const userService = new UserService();
    userService.getUserByEmail(req.decoded.email)
        .then(user => {
            if (user.length === 0) {
                return res.status(400).json({
                    success: false,
                    message: 'User not found'
                });
            }
            bcrypt.compare(oldPassword, user[0].password)
                .then(async isMatch => {
                    if (!isMatch) {
                        return res.status(400).json({
                            success: false,
                            message: 'Incorrect password'
                        });
                    }
                    user[0].password = await bcrypt.hash(newPassword, 10);
                    user[0].save();
                    return res.status(200).json({
                        success: true,
                        message: 'Password changed successfully'
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

const deleteAccount = (req, res) => {
    const userService = new UserService();
    userService.getUserByEmail(req.decoded.email)
        .then(user => {
            if (user.length === 0) {
                return res.status(400).json({
                    success: false,
                    message: 'User not found'
                });
            }
            user[0].destroy().then(() => {
                return res.status(200).json({
                    success: true,
                    message: 'Account deleted successfully'
                }).catch((err) => {
                    console.log(err);
                    return res.status(500).json({
                        success: false,
                        message: err.message
                    });
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

module.exports = {
    changePassword,
    deleteAccount,
};
