const openapi = require("@wesleytodd/openapi");

module.exports = openapi({
    openapi: '3.0.0',
    info: {
        title: 'Pandapp API Documentation',
        description: 'Generated docs from the pandapp-api project, you can find more about at [https://pandapp.thrallweb.fr](https://pandapp.thrallweb.fr) ',
        version: '1.0.0',
        contact: {
            name: 'Website',
            url: 'https://pandapp.thrallweb.fr'
        },
        servers: [
            {
                url: 'https://pandapp.thrallweb.fr/api/v1',
                description: 'Production'
            }
        ]
    }
});