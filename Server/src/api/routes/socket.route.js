
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
    responses: {
        200: {
            description: "Success",
            schema: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Success message",
                        example: "Device shutdown"
                    }
                }
            }
        },
        404: {
            description: "Device not found",
            schema: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Error message",
                        example: "Device not found"
                    }
                }
            }
        }
    }
}), (req, res) => controller.shutdown(req, res));

router.get("/volume/:action/:id", oapi.path({
    tags: ["socket"],
    summary: "Change volume",
    description: "Change volume",
    parameters: [
        {
            name: "id",
            in: "path",
            description: "Device ID",
            required: true,
            type: "string"
        },
        {
            name: "action",
            in: "path",
            description: "Action",
            required: true,
            type: "string"
        }
    ],
    responses: {
        200: {
            description: "Success",
            schema: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Success message",
                        example: "Volume changed"
                    }
                }
            }
        },
        400: {
            description: "Bad request",
            schema: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Error message",
                        example: "Bad request"
                    }
                }
            }
        },
        404: {
            description: "Device not found",
            schema: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Error message",
                        example: "Device not found"
                    }
                }
            }
        }
    }
}), (req, res) => controller.volume(req, res));

module.exports = router;
