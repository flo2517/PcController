

const shutdown = (req, res) => {
    let socket = req.app.get('client');
    console.log(socket);
    let id = req.params.id;
    console.log(id);
    if(socket[id]) {
        socket[id].emit('shutdown');
        res.status(200).json({
            message: 'Shutdown request sent'
        });
    } else {
        res.status(404).send({
            message: 'Socket not found'
        });
    }
}

module.exports = {
    shutdown
}