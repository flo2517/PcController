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

    deviceService.getByUuid(uuid).then(device => {
        console.log(device);
        if (device.length > 0) {
            return res.status(400).json({
                success: false,
                message: 'Device already exists'
            });
        } else {
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

    if (!uuid || !name ) {
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

    deviceService.delete(uuid).then(device => {
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

    deviceService.getAllByUser(req.decoded.id).then(devices => {
        let connected = req.app.get('client');
        let uuids = Object.keys(connected);
        devices.forEach((device, index) => {

            console.log(devices[index].dataValues);
            if(uuids.length === 0) {
                devices[index].dataValues.isOnline = false;
            } else if (uuids.find(client => {
                return client === device.dataValues.uuid
            })) {
                devices[index].dataValues.isOnline = true;
            } else {
                device[index].dataValues.isOnline = false;
            }
        });
        return res.status(200).json({
            success: true,
            message: 'Devices retrieved successfully',
            devices: devices
        });
    }).catch(err => {
        console.log("error bdd", err);
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