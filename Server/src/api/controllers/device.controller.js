const DeviceService = require("../services/device.service");

const add = (req, res) => {

    const {uuid, name} = req.body;

    console.log(req.decoded);

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


module.exports = {
    add
}