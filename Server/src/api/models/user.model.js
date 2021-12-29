const {sequelize} = require("../../config/db.config");
const { DataTypes , Model, Sequelize} = require("sequelize");

class User extends Model {}

User.init({
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    username: {
        type: Sequelize.STRING,
        allowNull: false,
    },
    email: {
        type: Sequelize.STRING,
        allowNull: false,
        unique: true,
    },
    password: {
        type: Sequelize.STRING,
        allowNull: false,
    },
}, {
    sequelize,
    modelName: "user",
    timestamps: false,
    createdAt: true
});



console.log("User model loaded", new User());



sequelize.define("user", User.attributes, User.options);



module.exports = User;


