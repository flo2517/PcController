const controller = require("../controllers/pages.controller");

let router = require("express").Router();

router.get("/", controller.home);

router.get('/download', controller.download);

router.get("/about", controller.about);

module.exports = router;