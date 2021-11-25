
const controller = require("../controllers/socket.controller");

let router = require("express").Router();

router.get("/shutdown/:id", (req, res) => controller.shutdown(req, res));

router.get("/volume/:action/:id", (req, res) => controller.volume(req, res));

module.exports = router;
