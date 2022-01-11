const openapi = require("@wesleytodd/openapi");

module.exports = openapi({
    openapi: '3.0.0',
    info: {
        title: 'Express App',
        description: 'Generated docs from an express api',
        version: '1.0.0'
    }
});