"use strict";

let express = require('express');
let app = express();

const server = require('http').createServer(app);
const io = require('socket.io')(server);

const CLIENT = {};

server.listen(8080, function() {
    console.log("C'est parti ! En attente de connexion sur le port 8080...");
});

io.on('connection', (socket) => {
   socket.on('source', (data) => {
       CLIENT[socket.id] = socket;
       console.log(`Client ${socket.id} connecté`);
   });

    socket.on('disconnect', (data) => {
        delete CLIENT[data.id];
    });

    app.get('/api/:id/test', (req, res) => {
        let id = req.params.id;
        let socket = CLIENT[id];
        if (socket) {
            socket.emit('test', {
                message: 'test'
            });
            res.status(200).send('ok');
        }
        else {
            res.status(404).send('not found');
        }
    });
});
