const {sequelize} = require("../../config/db.config");
const {Sequelize, Model} = require("sequelize");


class Device extends Model {}

Device.init({
    id: {
        type: Sequelize.INTEGER,
            primaryKey: true,
            autoIncrement: true,
    },
    uuid: {
        type: Sequelize.STRING(255),
            allowNull: false,
            unique: true
    },
    name: {
        type: Sequelize.STRING(255),
            allowNull: false
    }
}, {
    sequelize,
    modelName: "device"
});

sequelize.define("device", Device.attributes, Device.options);

module.exports = Device;