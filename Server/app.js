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


const oapi = require('./src/config/openapi.config');

app.use(oapi)






const {API_PORT} = process.env;
const port = process.env.PORT || API_PORT ;





app.use('/', require("./src/api/routes/socket.route"));
app.use('/', require("./src/api/routes/auth.route"));
app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "x-access-token, Origin, Content-Type, Accept");
    res.set("Content-Security-Policy", "default-src *; style-src 'self' http://* 'unsafe-inline'; script-src 'self' http://* 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:; font-src 'self' data:; connect-src 'self' ws://* https://*");
    next();
});

app.use('/device', require("./src/api/routes/device.route"));


server.listen(port, function() {
    console.log("C'est parti ! En attente de connexion sur le port "+port+"...");
});

console.log(oapi.document);

app.use('/doc', oapi.swaggerui);

io.on('connection', (socket) => {

    let token = null;
    socket.on('source', (data) => {
        console.log(socket.request.connection.remoteAddress);
        CLIENT[data.token] = socket;
        console.log(socket.handshake);
        console.log(`Client ${data.token} connecté`);
        token = data.token;
    });

    socket.on('disconnect', (data) => {
        delete CLIENT[token];
        console.log(CLIENT);
        console.log(`Client ${token} déconnecté`);
    });


});