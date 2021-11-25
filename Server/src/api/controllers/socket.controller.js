

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

const volume = (req, res) => {
    let socket = req.app.get('client');
    let id = req.params.id;
    let volume = req.body.action;
    if(socket[id]) {
        switch (volume) {
            case 'up':
                socket[id].emit('volumeUp');
                res.status(200).json({
                    message: 'Volume up request sent'
                });
                break;
            case 'down':
                socket[id].emit('volumeDown');
                res.status(200).json({
                    message: 'Volume down request sent'
                });
                break;
            case 'mute':
            case 'unmute':
                socket[id].emit('volumeMute');
                res.status(200).json({
                    message: 'Volume mute request sent'
                });
                break;
            case 'play':
            case 'pause':
                socket[id].emit('volumePlay');
                res.status(200).json({
                    message: 'Volume play request sent'
                });
                break;
            default:
                res.status(400).send({
                    message: 'Invalid action'
                });
                break;
        }
    } else {
        res.status(404).send({
            message: 'Socket not found'
        });
    }
}

module.exports = {
    shutdown,
    volume
}