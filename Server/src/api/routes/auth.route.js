
const controller = require("../controllers/auth.controller");

let router = require("express").Router();

router.get('/register', (req, res) => controller.register(req, res));

router.get('/login', (req, res) => controller.login(req, res));

module.exports = router;
