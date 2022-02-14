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
app.use(morgan('dev'));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/src/views'));

const server = require('http').createServer(app);

const io = require('socket.io')(server);
const CLIENT = {};

app.set('client', CLIENT);

require('dotenv').config({path : path.join(__dirname, '/.env')});

const oapi = require('./src/config/openapi.config');
const uuidValidation = require("./src/api/validations/uudi.validation");

app.use(oapi)

const {API_PORT} = process.env;
const port = process.env.PORT || API_PORT ;

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "x-access-token, Origin, Content-Type, Accept");
    res.set("Content-Security-Policy", "default-src *; style-src 'self' https://* 'unsafe-inline'; script-src 'self' https://* 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:; font-src 'self' data:; connect-src 'self' ws://* https://*");
    next();
});

app.use('/', require("./src/api/routes/socket.route"));
app.use('/', require("./src/api/routes/auth.route"));
app.use('/', require("./src/api/routes/pages.route"));
app.use('/device', require("./src/api/routes/device.route"));
app.use('/user', require("./src/api/routes/user.route"));
app.use('/doc', oapi.swaggerui);


server.listen(port, function() {
    console.log("C'est parti ! En attente de connexion sur le port "+port+"...");
});


const jwt = require("jsonwebtoken");
const {TokenExpiredError} = require("jsonwebtoken");
io.on('connection', (socket) => {

    let token = null;
    socket.on('source', (data) => {
        // console.log(socket.request.connection.remoteAddress);
        // console.log(socket.handshake);

        console.log(data);

        let parse = JSON.parse(data);
        console.log(parse.token);
        console.log(parse.user);
        
        token = parse.token;
        jwt.verify(parse.user, process.env.TOKEN_KEY, (err, decoded) => {
            if(err) {
                console.log(err);
                if (err instanceof TokenExpiredError) {
                    socket.emit('error', { message: "Unauthorized! Access Token was expired!" });
                    return;
                }
                socket.emit('error', { message: 'Failed to authenticate token.' });
                return;
            }
            console.log(decoded);

            uuidValidation(parse.token, decoded.id)
                .then(() => {
                    CLIENT[parse.token] = socket;
                    console.log(`Client ${parse.token} connecté`);

                })
                .catch((err) => {
                    console.log(err);
                    socket.emit('error', err);
                    token=null;
                });
        });
    });

    socket.on('disconnect', () => {
        delete CLIENT[token];
        console.log(CLIENT);
        console.log(`Client ${token} déconnecté`);
    });

});

// const {sendVerifyMail} = require("./src/api/services/email.service");
//
// sendVerifyMail('jeandenans.florian@gmail.com', 'yolo');
