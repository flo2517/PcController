const UserService = require("../services/user.service");
const {sequelize} = require("../../config/db.config");


const register = async (req, res) => {
    let userService;
    try {
        // const { email, username, password } = req.body;
        // if(!email || !username || !password){
        //     return res.status(400).json({
        //         success: false,
        //         message: 'Please enter all fields'
        //     });
        // }
        userService = new UserService();
        const user = await userService.createUser({
            email: "john@doe.fr",
            username: "john",
            password: "pass"
        });
        console.log(user);
        return res.status(200).json({
            success: true,
            message: 'User created',
            user
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
    res.send('login');
};

module.exports = {
    login,
    register
};