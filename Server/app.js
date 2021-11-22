"use strict";

let express = require('express');
let app = express();

const server = require('http').createServer(app);
const io = require('socket.io')(server);

const CLIENT = {};

app.set('client', CLIENT);

server.listen(8080, function() {
    console.log("C'est parti ! En attente de connexion sur le port 8080...");
});

require('./src/api/routes/socket.route')(app);


io.on('connection', (socket) => {
    socket.on('source', (data) => {
        CLIENT[socket.id] = socket;
        console.log(socket.handshake);
        console.log(`Client ${socket.id} connecté`);
    });

    socket.on('disconnect', (data) => {
        delete CLIENT[data.id];
    });


});