const oapi = require("../../config/openapi.config");
const auth = require("../middlewares/auth.middleware");
const controller = require("../controllers/user.controller");
const {error400, error401, error403, error500} = require("../helpers/errorsList.helper");


let router = require("express").Router();

router.post('/changePassword', oapi.path({
    tags: ['User'],
    summary: 'Change password',
    description: 'Change password',
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
            name: "body",
            in: "body",
            description: "body",
            required: true,
            schema: {
                type: "object",
                properties: {
                    oldPassword: {
                        type: "string"
                    },
                    newPassword: {
                        type: "string"
                    }
                }
            }
        }
    ],
    responses: {
        "200": {
            description: "Success",
            content: {
                "application/json": {
                    schema: {
                        type: "object",
                        properties: {
                            success: {
                                type: "boolean",
                                description: "Success",
                                example: true
                            },
                            message: {
                                type: "string",
                                description: "Message",
                                example: "Password changed successfully"
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
}), auth,  (req, res) => controller.changePassword(req, res));

// router.post('/forgotPassword', oapi.path({}), (req, res) => controller.forgotPassword(req, res));

router.post('/deleteAccount', oapi.path({
    tags: ['User'],
    summary: 'Delete account',
    description: 'Delete account',
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
            name: "body",
            in: "body",
            description: "body",
            required: true,
            schema: {
                type: "object",
                properties: {
                    password: {
                        type: "string"
                    }
                }
            }
        }
    ],
    responses: {
        "200": {
            description: "Success",
            content: {
                "application/json": {
                    schema: {
                        type: "object",
                        properties: {
                            success: {
                                type: "boolean",
                                description: "Success",
                                example: true
                            },
                            message: {
                                type: "string",
                                description: "Message",
                                example: "Account deleted successfully"
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
}), auth,  (req, res) => controller.deleteAccount(req, res));

module.exports = router;