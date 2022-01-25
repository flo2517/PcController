const DeviceService = require("../services/device.service");

const add = (req, res) => {

    const {uuid, name} = req.body;


    if (!uuid || !name) {
        return res.status(400).json({
            success: false,
            message: 'Please provide a uuid and name'
        });
    }

    const deviceService = new DeviceService();

    deviceService.create({
        uuid: uuid,
        name: name,
        userId: req.decoded.id
    }).then(device => {
        return res.status(200).json({
            success: true,
            message: 'Device added successfully',
            device
        });
    }).catch(err => {
        return res.status(500).json({
            success: false,
            message: 'Error adding device',
            error: err
        });
    });
}


const update = (req, res) => {

    const {uuid, name} = req.body;

    if (!uuid || !name) {
        return res.status(400).json({
            success: false,
            message: 'Please provide a uuid and name'
        });
    }

    const deviceService = new DeviceService();

    deviceService.update({
        uuid: uuid,
        name: name,
        userId: req.decoded.id
    }).then(device => {
        return res.status(200).json({
            success: true,
            message: 'Device updated successfully',
            device
        });
    }).catch(err => {
        return res.status(500).json({
            success: false,
            message: 'Error updating device',
            error: err
        });
    });
}
const del = (req, res) => {

    const {uuid} = req.body;

    if (!uuid) {
        return res.status(400).json({
            success: false,
            message: 'Please provide a uuid'
        });
    }

    const deviceService = new DeviceService();

    deviceService.delete({
        uuid: uuid,
        userId: req.decoded.id
    }).then(device => {
        return res.status(200).json({
            success: true,
            message: 'Device deleted successfully',
            device
        });
    }).catch(err => {
        return res.status(500).json({
            success: false,
            message: 'Error deleting device',
            error: err
        });
    });
}


const getAll = (req, res) => {

    const deviceService = new DeviceService();

    deviceService.getAll(req.decoded.id).then(devices => {
        return res.status(200).json({
            success: true,
            message: 'Devices retrieved successfully',
            devices: devices
        });
    }).catch(err => {
        return res.status(500).json({
            success: false,
            message: 'Error retrieving devices',
            error: err
        });
    });
}

module.exports = {
    add,
    update,
    del,
    getAll
}