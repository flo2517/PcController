
const controller = require("../controllers/auth.controller");

let router = require("express").Router();


router.post('/register', (req, res) => controller.register(req, res));

router.post('/login', (req, res) => controller.login(req, res));

router.post('/refreshtoken', (req, res) => controller.refreshToken(req, res));

module.exports = router;
