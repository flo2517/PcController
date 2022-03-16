const controller = require("../controllers/pages.controller");

let router = require("express").Router();

router.get("/", controller.home);

router.get('/download', controller.download);

router.get('/download/:file', controller.downloadFile);

router.get("/about", controller.about);

router.get("/comments", controller.comments);

router.post("/comments", controller.addComment);

module.exports = router;