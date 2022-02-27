const Sequelize = require('sequelize');
const {Device} = require("../models/index");

class DeviceService {
    constructor() {

    }

    async getAllByUser(userId) {
        return await Device.findAll(
            {
                where: {
                    userId: userId
                }
            }
        );
    }

    async getByUuid(uuid) {
        return await Device.findAll(
            {
                where: {
                    uuid: uuid
                }
            }
        );
    }

    async getById(id, userId) {
        return Device.findOne({
            where: {
                id: id,
                userId: userId
            }
        });
    }

    async create(device) {
        return Device.create(device);
    }

    async update(device) {
        return await Device.update(device, {
            where: {
                uuid: device.uuid
            }
        });
    }

    async delete(uuid) {
        return await Device.destroy({
            where: {
                uuid: uuid
            }
        });
    }
}

module.exports = DeviceService;