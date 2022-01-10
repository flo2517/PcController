
const controller = require("../controllers/socket.controller");
const oapi = require("../../config/openapi.config");

let router = require("express").Router();

router.get("/shutdown/:id", oapi.path({
    tags: ["socket"],
    summary: "Shutdown a device",
    description: "Shutdown a device",
    parameters: [
        {
            name: "id",
            in: "path",
            description: "Device ID",
            required: true,
            type: "string"
        }
    ],
}), (req, res) => controller.shutdown(req, res));

router.get("/volume/:action/:id", (req, res) => controller.volume(req, res));

module.exports = router;
