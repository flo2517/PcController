
const shutdown = (req, res) => {
    let socket = req.app.get('client');
    console.log(socket);
    let id = req.params.id;
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
    let volume = req.params.action;
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

const lock = (req, res) => {
    let socket = req.app.get('client');
    let id = req.params.id;
    if(socket[id]) {
        socket[id].emit('lock');
        res.status(200).json({
            message: 'Lock request sent'
        });
    } else {
        res.status(404).send({
            message: 'Socket not found'
        });
    }
}

const next = (req, res) => {
    let socket = req.app.get('client');
    let id = req.params.id;
    if(socket[id]) {
        socket[id].emit('next');
        res.status(200).json({
            message: 'Next music request sent'
        });
    } else {
        res.status(404).send({
            message: 'Socket not found'
        });
    }
}

const previous = (req, res) => {
    let socket = req.app.get('client');
    let id = req.params.id;
    if(socket[id]) {
        socket[id].emit('previous');
        res.status(200).json({
            message: 'Previous music request sent'
        });
    } else {
        res.status(404).send({
            message: 'Socket not found'
        });
    }
}

const arrow = (req, res) => {
    let socket = req.app.get('client');
    let id = req.params.id;
    let arrow = req.params.action;
    if(socket[id]) {
        switch (arrow) {
            case 'up':
                socket[id].emit('up');
                res.status(200).json({
                    success: true,
                    message: 'Arrow up request sent'
                });
                break;
            case 'down':
                socket[id].emit('down');
                res.status(200).json({
                    success: true,
                    message: 'Arrow down request sent'
                });
                break;
            case 'left':
                socket[id].emit('left');
                res.status(200).json({
                    success: true,
                    message: 'Arrow left request sent'
                });
                break;
            case 'right':
                socket[id].emit('right');
                res.status(200).json({
                    success: true,
                    message: 'Arrow right request sent'
                });
                break;
            default:
                res.status(400).send({
                    success: false,
                    message: 'Invalid action'
                });
                break;
        }
    } else {
        res.status(404).send({
            success: false,
            message: 'Socket not found'
        });
    }
}

module.exports = {
    shutdown,
    volume,
    lock,
    next,
    previous,
    arrow
}