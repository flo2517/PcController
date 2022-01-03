const User = require('./user.model');
const RefreshToken = require('./refreshToken.model');
const Device = require('./device.model');
const {sequelize} = require("../../config/db.config");

User.hasOne(sequelize.models.refreshToken, {foreignKey: "userId", sourceKey: "id"});

RefreshToken.belongsTo(sequelize.models.user, {
    foreignKey: "userId",
    targetKey: "id"
});

User.hasMany(sequelize.models.device, {foreignKey: "userId", sourceKey: "id"});

Device.belongsTo(sequelize.models.user, {
    foreignKey: "userId",
    targetKey: "id"
});

User.sync({force: true});
RefreshToken.sync({force: true});
Device.sync({force: true});





module.exports =  {User, RefreshToken};