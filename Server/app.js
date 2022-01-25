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

const oapi = require('./src/config/openapi.config');
const uuidValidation = require("./src/api/validations/uudi.validation");

app.use(oapi)

const {API_PORT} = process.env;
const port = process.env.PORT || API_PORT ;

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "x-access-token, Origin, Content-Type, Accept");
    res.set("Content-Security-Policy", "default-src *; style-src 'self' http://* 'unsafe-inline'; script-src 'self' http://* 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:; font-src 'self' data:; connect-src 'self' ws://* https://*");
    next();
});

app.use('/', require("./src/api/routes/socket.route"));
app.use('/', require("./src/api/routes/auth.route"));
app.use('/device', require("./src/api/routes/device.route"));
app.use('/user', require("./src/api/routes/user.route"));
app.use('/doc', oapi.swaggerui);


server.listen(port, function() {
    console.log("C'est parti ! En attente de connexion sur le port "+port+"...");
});


const jwt = require("jsonwebtoken");
io.on('connection', (socket) => {

    let token = null;
    socket.on('source', (data) => {
        console.log(socket.request.connection.remoteAddress);
        console.log(socket.handshake);
        let user = {}
        jwt.verify(data.user, process.env.TOKEN_KEY, (err, decoded) => {
            if(err) {
                console.log(err);
                if (err instanceof TokenExpiredError) {
                    socket.emit('error', { message: "Unauthorized! Access Token was expired!" });
                    return;
                }
                socket.emit('error', { message: 'Failed to authenticate token.' });
                return;
            }
            // console.log(decoded);
            user = decoded
        });
        uuidValidation(data.token, user.id)
            .then(() => {
                CLIENT[data.token] = socket;
                console.log(`Client ${data.token} connecté`);
                token = data.token;
            })
            .catch((err) => {
                console.log(err);
                socket.emit('error', err);
            });
    });

    socket.on('disconnect', () => {
        delete CLIENT[token];
        console.log(CLIENT);
        console.log(`Client ${token} déconnecté`);
    });

});