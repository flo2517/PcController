
const error400 = {
    description: "Bad request",
    content: {
        'application/json': {
            schema: {
                type: 'object',
                properties: {
                    success: {
                        type: "boolean",
                        description: "Success",
                        example: false
                    },
                    message: {
                        type: "string",
                        description: "Message",
                        example: "Bad request"
                    }
                }
            }
        }
    }
}

const error401= {
    description: "Unauthorized",
    content: {
        'application/json': {
            schema: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Error message",
                        example: "Unauthorized"
                    }
                }
            }
        }
    }
}

const error403= {
    description: "Forbidden",
    content: {
        'application/json': {
            schema: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Error message",
                        example: "Forbidden"
                    }
                }
            }
        }
    }
}

const error500 = {
    description: "Internal server error",
    content: {
        'application/json': {
            schema: {
                type: 'object',
                properties: {
                    success: {
                        type: "boolean",
                        description: "Success",
                        example: false
                    },
                    message: {
                        type: "string",
                        description: "Message",
                        example: "Internal server error"
                    }
                }
            }
        }
    }
}

module.exports = {
    error401,
    error403,
    error500
}