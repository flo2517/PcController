
const add = (req, res) => {
    res.status(200).json({
        message: 'Device added successfully'
    });
}

module.exports = {
    add
}