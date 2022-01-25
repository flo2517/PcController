const UserService = require("../services/user.service");
const DeviceService = require("../services/device.service");


const uuidValidation = (uuid, userId) => {

    if (!uuid) {
        throw 'UUID is required';
    }

    if (!userId) {
        throw 'User ID is required';
    }

    const deviceService = new DeviceService();

    return deviceService.getAll(userId)
        .then(devices => {
            if (!devices || !devices.length) {
                throw {message: 'User has no devices'};
            }

            const device = devices.find(device => device.dataValues.uuid === uuid);

            if (!device) {
                throw {message: 'Device not found'};
            }

            return device;
        });
}

module.exports = uuidValidation;