
const controller = require('../controllers/device.controller');

const router = require("express").Router();

const auth = require('../middlewares/auth.middleware');
const oapi = require("../../config/openapi.config");
const {error400, error401, error403, error500} = require('../helpers/errorsList.helper');


router.post("/add", oapi.path({
    tags: ["Device"],
    summary: "Add a new device",
    description: "Add a new device",
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
        in: "body",
        name: "device",
        description: "Device object",
        required: true,
        schema: {
            type: "object",
            properties: {
                uuid: {
                    type: "string",
                    description: "Device uuid",
                    example: "5e8f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8"
                },
                name: {
                    type: "string",
                    description: "Device name",
                    example: "My device"
                },
            }
        }
    }],
    responses: {
        200: {
            description: "Device added",
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: "boolean",
                                description: "Success",
                                example: true
                            },
                            message: {
                                type: "string",
                                description: "Message",
                                example: "Device added"
                            },
                            device: {
                                type: "object",
                                description: "Device",
                                example: {
                                    id: 1,
                                    uuid: "5e8f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8",
                                    name: "My device",
                                    userId: 1,
                                    createdAt: "2020-01-01T00:00:00.000Z",
                                    updatedAt: "2020-01-01T00:00:00.000Z"
                                }
                            }
                        }
                    }
                }
            }
        },
        400: error400,
        401: error401,
        403: error403,
        500: error500
    }
}), auth, (req, res) => {
    controller.add(req, res);
});

router.post("/update", oapi.path({
    tags: ["Device"],
    summary: "Update a device",
    description: "Update a device",
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
        in: "body",
        name: "device",
        description: "Device object",
        required: true,
        schema: {
            type: "object",
            properties: {
                uuid: {
                    type: "string",
                    description: "Device uuid",
                    example: "5e8f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8"
                },
                name: {
                    type: "string",
                    description: "Device name",
                    example: "My device"
                },
            }
        }
    }],
    responses: {
        200: {
            description: "Device updated",
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: "boolean",
                                description: "Success",
                                example: true
                            },
                            message: {
                                type: "string",
                                description: "Message",
                                example: "Device updated"
                            },
                            device: {
                                type: "object",
                                description: "Device",
                                example: {
                                    id: 1,
                                    uuid: "5e8f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8",
                                    name: "My device",
                                    userId: 1,
                                    createdAt: "2020-01-01T00:00:00.000Z",
                                }
                            }
                        }
                    }
                }
            }
        },
        400: error400,
        401: error401,
        403: error403,
        500: error500
    }
}), auth, (req, res) => {
    controller.update(req, res);
});

router.post("/delete", oapi.path({
    tags: ["Device"],
    summary: "Delete a device",
    description: "Delete a device",
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
            in: "body",
            name: "device",
            description: "Device object",
            required: true,
            schema: {
                type: "object",
                properties: {
                    uuid: {
                        type: "string",
                        description: "Device uuid",
                        example: "5e8f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8"
                    }
                }
            }
        }],
    responses: {
        200: {
            description: "Device deleted",
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: "boolean",
                                description: "Success",
                                example: true
                            },
                            message: {
                                type: "string",
                                description: "Message",
                                example: "Device deleted"
                            }
                        }
                    }
                }
            }
        },
        400: error400,
        401: error401,
        403: error403,
        500: error500
    }
}), auth, (req, res) => {
    controller.del(req, res);
});

router.get("/getAll", oapi.path({
    tags: ["Device"],
    summary: "Add a new device",
    description: "Add a new device",
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
    ],
    responses: {
        200: {
            description: "Device added",
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: "boolean",
                                description: "Success",
                                example: true
                            },
                            message: {
                                type: "string",
                                description: "Message",
                                example: "Success"
                            },
                            devices: {
                                type: "array",
                                description: "Devices",
                                example: [
                                    {
                                        id: 1,
                                        uuid: "5e8f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8",
                                        name: "My device",
                                        userId: 1
                                    },
                                    {
                                        id: 2,
                                        uuid: "5e8f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8",
                                        name: "My device",
                                        userId: 1
                                    }
                                ]
                            }
                        }
                    }
                }
            }
        },
        400: error400,
        401: error401,
        403: error403,
        500: error500
    }
}), auth, (req, res) => {
    controller.getAll(req, res);
});

module.exports = router;


