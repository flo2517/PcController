const controller = require("../controllers/socketApi.controller");
const oapi = require("../../config/openapi.config");
const auth = require('../middlewares/auth.middleware');
const socket = require('../middlewares/socket.middleware');
const {error401, error403, error400} = require("../helpers/errorsList.helper");

let router = require("express").Router();

router.get("/shutdown/:id", auth, socket, oapi.path({
    tags: ["socket"],
    summary: "Shutdown a device",
    description: "Shutdown a device",
    parameters: [
        {
            name: "x-access-token",
            in: "header",
            description: "header",
            required: true,
            schema: {
                type: "string"

            }
        },
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
            content: {
                'application/json': {
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
                }
            }
        },
        404: {
            description: "Device not found",
            content: {
                'application/json': {
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
        }
    }
}), (req, res) => controller.shutdown(req, res));

router.get("/volume/:action/:id", auth, socket, oapi.path({
    tags: ["socket"],
    summary: "Change volume",
    description: "Change volume",
    parameters: [
        {
            name: "x-access-token",
            in: "header",
            description: "header",
            required: true,
            schema: {
                type: "string"

            }
        },
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
            content: {
                'application/json': {
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
                }
            }
        },
        400: {
            description: "Bad request",
            content: {
                'application/json': {
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
                }
            }
        },
        404: {
            description: "Device not found",
            content: {
                'application/json': {
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
        }
    }
}), (req, res) => controller.volume(req, res));

router.get("/lock/:id", auth, socket, oapi.path({
    tags: ["socket"],
    summary: "Lock device",
    description: "Lock device",
    parameters: [
        {
            name: "x-access-token",
            in: "header",
            description: "header",
            required: true,
            schema: {
                type: "string"

            }
        },
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
            content: {
                'application/json': {
                    schema: {
                        type: "object",
                        properties: {
                            message: {
                                type: "string",
                                description: "Success message",
                                example: "Device locked"
                            }
                        }
                    }
                }
            }
        },
        400: error400,
        401: error401,
        403: error403,
        404: {
            description: "Device not found",
            content: {
                'application/json': {
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
        }
    }
}), (req, res) => controller.lock(req, res))

router.get("/next-music/:id", auth, socket, oapi.path({
    tags: ["socket"],
    summary: "Next music",
    description: "Next music",
    parameters: [
        {
            name: "x-access-token",
            in: "header",
            description: "header",
            required: true,
            schema: {
                type: "string"

            }
        },
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
            content: {
                'application/json': {
                    schema: {
                        type: "object",
                        properties: {
                            message: {
                                type: "string",
                                description: "Success message",
                                example: "Next music"
                            }
                        }
                    }
                }
            }
        },
        400: error400,
        401: error401,
        403: error403,
        404: {
            description: "Device not found",
            content: {
                'application/json': {
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
        }
    }
}), controller.next);

router.get("/previous-music/:id", auth, socket, oapi.path({
    tags: ["socket"],
    summary: "Previous music",
    description: "Previous music",
    parameters: [
        {
            name: "x-access-token",
            in: "header",
            description: "header",
            required: true,
            schema: {
                type: "string"

            }
        },
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
            content: {
                'application/json': {
                    schema: {
                        type: "object",
                        properties: {
                            message: {
                                type: "string",
                                description: "Success message",
                                example: "Previous music"
                            }
                        }
                    }
                }
            }
        },
        400: error400,
        401: error401,
        403: error403,
        404: {
            description: "Device not found",
            content: {
                'application/json': {
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
        }
    }
}), controller.previous);

module.exports = router;
