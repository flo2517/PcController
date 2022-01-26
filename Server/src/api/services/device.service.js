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

    async update(id, device) {
        return await this.device.update(device, {
            where: {
                id: id
            }
        });
    }

    async delete(id) {
        return await this.device.destroy({
            where: {
                id: id
            }
        });
    }
}

module.exports = DeviceService;