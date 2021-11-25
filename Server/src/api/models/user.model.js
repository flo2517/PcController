const {sequelize} = require("../../config/db.config");
const { DataTypes , Model, Sequelize} = require("sequelize");

class User extends Model {}

User.init({
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    username: {
        type: DataTypes.STRING,
        allowNull: false
    },
    email: {
        type: DataTypes.STRING,
        allowNull: false,
        unique: true
    },
    password: {
        type: DataTypes.STRING,
        allowNull: false
    },
    createdAt: {
        type: DataTypes.DATE,
        allowNull: false
    },
}, {
    sequelize,
    modelName: "user",
    timestamps: false
});

User.sync();

module.exports = sequelize.define("user", User.attributes, User.options);

