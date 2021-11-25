"use strict";

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const path = require("path");
let app = express();

app.use(helmet());

app.use(bodyParser.json({ limit: '100mb' }));
app.use(bodyParser.urlencoded({ extended: true, limit: '100mb', parameterLimit: 1000000 }));
app.use(cors());
app.use(morgan('combined'));
const server = require('http').createServer(app);

const io = require('socket.io')(server);
const CLIENT = {};

app.set('client', CLIENT);

require('dotenv').config({path : path.resolve(process.cwd(), './Server/.env')});


console.log(process.cwd());

const {API_PORT} = process.env;
const port = process.env.PORT || API_PORT ;



server.listen(port, function() {
    console.log("C'est parti ! En attente de connexion sur le port "+port+"...");
});

app.use('/', require("./src/api/routes/socket.route"));
app.use('/', require("./src/api/routes/auth.route"));




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