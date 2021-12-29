const {sequelize} = require("../../config/db.config");
const { DataTypes , Model, Sequelize} = require("sequelize");
const { v4: uuidv4 } = require("uuid");

class RefreshToken extends Model {}

RefreshToken.init({
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
        unique: true
    },
    token: {
        type: Sequelize.STRING,
        allowNull: false,
        unique: true,
    },
    expiryDate: {
        type: Sequelize.DATE,
        allowNull: false
    },
}, {
    sequelize,
    modelName: "refreshToken"
});

RefreshToken.createToken = async function(user){
    let expiredAt = new Date();
    expiredAt.setSeconds(expiredAt.getSeconds() + parseInt(process.env.JWT_REFRESH_EXPIRATION_TIME));

    let _token = uuidv4();

    console.log(user);

    return this.create({
        token: _token,
        userId: user.id,
        expiryDate: expiredAt.getTime()
    });
}

RefreshToken.verifyExpiration = (token) => {
    return token.expiryDate.getTime() < new Date().getTime();
}

sequelize.define("refreshToken", RefreshToken.attributes, RefreshToken.options);


module.exports = RefreshToken;
