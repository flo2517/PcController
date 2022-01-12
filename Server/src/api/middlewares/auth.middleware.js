const jwt = require('jsonwebtoken');
const { TokenExpiredError } = jwt;
const config = process.env

const verifyToken = (req, res, next) => {
    const token = req.body.token || req.query.token || req.headers['x-access-token'];
    if(!token) {
        return res.status(403).send({
            success: false,
            message: 'No token provided.'
        });
    }
    // console.log(token);
    jwt.verify(token, config.TOKEN_KEY, (err, decoded) => {
        if(err) {
            console.log(err);
            if (err instanceof TokenExpiredError) {
                return res.status(401).send({ message: "Unauthorized! Access Token was expired!" });
            }
            return res.status(401).send({
                success: false,
                message: 'Failed to authenticate token.'
            });
        }
        // console.log(decoded);
        req.decoded = decoded;
        next();
    });
}


module.exports = verifyToken;