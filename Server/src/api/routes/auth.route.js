
const controller = require("../controllers/auth.controller");

let router = require("express").Router();

const oapi = require("../../config/openapi.config");

router.post('/register', oapi.path({
    tags: ['Auth'],
    summary: 'Register a new user',
    description: 'Register a new user',
    parameters: [
        {
            name: 'body',
            in: 'body',
            description: 'User object that needs to be added to the store',
            required: true,
            schema: {
                type: 'object',
                properties: {
                    email: {
                        type: 'string',
                        format: 'email',
                        example: 'john@doe.fr'
                    },
                    username: {
                        type: 'string',
                        example: 'johndoe',
                        description: 'Username of the user'
                    },
                    password: {
                        type: 'string',
                        example: 'johndoe',
                        description: 'Password of the user'
                    }
                }
            }
        }
    ],
    responses: {
        200: {
            description: 'Success',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            token: {
                                type: 'string',
                                description: 'JWT token',
                                example: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVlYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQ'
                            },
                            message: {
                                type: 'string',
                                description: 'Success message',
                                example: 'User registered'
                            },
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: true
                            }
                        }
                    }
                }
            }
        },
        400: {
            description: 'Bad Request',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            message: {
                                type: 'string',
                                description: 'Error message',
                                example: 'Invalid user input'
                            },
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: false
                            }
                        }
                    }
                }
            }
        },
        500: {
            description: 'Internal Server Error',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            message: {
                                type: 'string',
                                description: 'Error message',
                                example: 'Internal Server Error'
                            },
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: false
                            }
                        }
                    }
                }
            }
        }
    }
}), (req, res) => controller.register(req, res));

router.post('/login', oapi.path({
    tags: ['Auth'],
    summary: 'Login a user',
    description: 'Login a user',
    parameters: [
        {
            in: 'body',
            name: 'body',
            description: 'User credentials',
            required: true,
            schema: {
                type: 'object',
                properties: {
                    email: {
                        type: 'email',
                        example: 'john@doe.fr',
                        description: 'Username of the user'
                    },
                    password: {
                        type: 'string',
                        example: 'johndoe',
                        description: 'Password of the user'
                    }
                }
            }
        }
    ],
    responses:  {
        200: {
            description: 'Success',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            token: {
                                type: 'string',
                                description: 'JWT token',
                                example: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVlYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYzQwMzYwYz'
                            },
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: true
                            },
                            message: {
                                type: 'string',
                                description: 'Success message',
                                example: 'Successfully logged in'
                            },
                            refreshToken: {
                                type: 'object',
                                description: 'Refresh token',
                                example: {
                                    id: 1,
                                    token: 'd276e84a-10cf-4533-a5c4-c9cf2b5c5535',
                                    expiryDate: '2019-12-31T23:59:59.999Z',
                                    updatedAt: '2019-12-31T23:59:59.999Z',
                                    createdAt: '2019-12-31T23:59:59.999Z'
                                }
                            }
                        }
                    }
                }
            }
        },
        400: {
            description: 'Bad request',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: false
                            },
                            message: {
                                type: 'string',
                                description: 'Error message',
                                example: 'Invalid credentials'
                            }
                        }
                    }
                }
            }
        },
        500: {
            description: 'Internal server error',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: false
                            },
                            message: {
                                type: 'string',
                                description: 'Error message',
                                example: 'Internal server error'
                            }
                        }
                    }
                }
            }
        }
    }
}), (req, res) => controller.login(req, res));

router.post('/refreshtoken', oapi.path({
    tags: ['Auth'],
    summary: 'Refresh token',
    description: 'Refresh token',
    parameters: [
        {
            name: 'Authorization',
            in: 'body',
            description: 'Bearer token',
            required: true,
            schema: {
                type: 'object',
                properties: {
                    refreshToken: {
                        type: 'string',
                        description: 'Refresh token',
                        example: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJqb2huQGRvZS5mciIsInVzZXJuYW1lIjoiam9obiIsImlhdCI6MTY0MTMwODg4OCwiZXhwIjoxNjQxMzA4ODk1fQ.OLZ_TpObHBxuv4JDC2n3ed3e1rIFCR4VKjre-wlb0eg'
                    }
                }

            }
        }
    ],
    responses: {
        200: {
            description: 'Success',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: true
                            },
                            message: {
                                type: 'string',
                                description: 'Success message',
                                example: 'Successfully logged in'
                            },
                            accessToken: {
                                type: 'string',
                                description: 'Access token',
                                example: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJqb2huQGRvZS5mciIsInVzZXJuYW1lIjoiam9obiIsImlhdCI6MTY0MTMwODg4OCwiZXhwIjoxNjQxMzA4ODk1fQ.OLZ_TpObHBxuv4JDC2n3ed3e1rIFCR4VKjre-wlb0eg'
                            },
                            refreshToken: {
                                type: 'object',
                                description: 'Refresh token',
                                example: {
                                    id: 1,
                                    token: 'd276e84a-10cf-4533-a5c4-c9cf2b5c5535',
                                    expiryDate: '2019-12-31T23:59:59.999Z',
                                    updatedAt: '2019-12-31T23:59:59.999Z',
                                    createdAt: '2019-12-31T23:59:59.999Z'
                                }
                            }
                        }
                    }
                }
            }
        },
        400: {
            description: 'Bad request',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: false
                            },
                            message: {
                                type: 'string',
                                description: 'Error message',
                                example: 'Invalid credentials'
                            }
                        }
                    }
                }
            }
        },
        403: {
            description: 'Forbidden',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: false
                            },
                            message: {
                                type: 'string',
                                description: 'Error message',
                                example: 'Refresh token has expired. Please login again'
                            }
                        }
                    }
                }
            }
        },
        500: {
            description: 'Internal server error',
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            success: {
                                type: 'boolean',
                                description: 'Success status',
                                example: false
                            },
                            message: {
                                type: 'string',
                                description: 'Error message',
                                example: 'Internal server error'
                            }
                        }
                    }
                }
            }
        }
    }

}), (req, res) => controller.refreshToken(req, res));

module.exports = router;
