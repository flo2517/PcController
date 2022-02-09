const Sequelize = require('sequelize');
const {Device} = require("../models/index");

class DeviceService {
    constructor() {
        this.device = Device;
    }

    async getAll(userId) {
        return this.device.findAll(
            {
                where: {
                    userId: userId
                }
            }
        );
    }

    async getByUuid(uuid) {
        return this.device.findAll(
            {
                where: {
                    uuid: uuid
                }
            }
        );
    }

    async getById(id, userId) {
        return this.device.findOne({
            where: {
                id: id,
                userId: userId
            }
        });
    }

    async create(device) {
        return this.device.create(device);
    }

    async update(device) {
        return await this.device.update(device, {
            where: {
                uuid: device.uuid
            }
        });
    }

    async delete(uuid) {
        return await this.device.destroy({
            where: {
                uuid: uuid
            }
        });
    }
}

module.exports = DeviceService;