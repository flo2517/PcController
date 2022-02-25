const uuidValidation = require("../validations/uudi.validation");

const validId = (req, res, next) => {
    if (!(req.params.id || req.body.uuid)) {
        return res.status(400).json({
          status: 400,
          error: 'Bad Request',
          message: 'Please provide a valid id'
        });
    }

    let id = req.params.id || req.body.uuid;
    let userId = req.decoded.id ;

    uuidValidation(id, userId).catch(err => {
        console.log(err);
        return res.status(400).json({
            success: false,
            message: err.message
        });
    }).then(() => {
        next();
    });
    
};

module.exports = validId;