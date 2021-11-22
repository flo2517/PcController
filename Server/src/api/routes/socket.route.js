module.exports = app => {
    const controller = require("../controllers/socket.controller");

    let router = require("express").Router();

    router.get("/shutdown/:id", (req, res) => controller.shutdown(req, res));

    app.use("/", router);
}