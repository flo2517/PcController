
const add = (req, res) => {

    const {token, uuid} = req.body;
    

    res.status(200).json({
        message: 'Device added successfully'
    });
}


module.exports = {
    add
}