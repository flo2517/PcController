const User = require('./user.model');
const RefreshToken = require('./refreshToken.model');
const {sequelize} = require("../../config/db.config");
const Device = require("./device.model");

User.hasOne(sequelize.models.refreshToken, {
    foreignKey: "userId",
    sourceKey: "id",
    onDelete: "CASCADE",
});

RefreshToken.belongsTo(sequelize.models.user, {
    foreignKey: "userId",
    targetKey: "id"
});

User.hasMany(sequelize.models.device, {
    foreignKey: "userId",
    sourceKey: "id",
    onDelete: "CASCADE",
});

Device.belongsTo(sequelize.models.user, {
    foreignKey: "userId",
    targetKey: "id"
});

RefreshToken.sync({force: false});
Device.sync({force: false});
User.sync({force: false});

module.exports =  {User, RefreshToken, Device};