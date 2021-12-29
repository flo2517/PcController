
const controller = require('../controllers/device.controller');

const router = require("express").Router();

const auth = require('../middlewares/auth.middleware');

router.post("/add", auth, (req, res) => {
    controller.add(req, res);
});

module.exports = router;


