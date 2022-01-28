
module.exports = (subdomain, fn) => {

    if(!subdomain || typeof subdomain !== 'string') {
        throw new Error('Subdomain is required and must be a string');
    }

    // if(!fn || typeof fn !== 'function' || fn.length < 2) {
    //     throw new Error('Callback is required and must be a function that handles 3 arguments : fn(req, res, next)');
    // }

    return (req, res, next) => {
        console.log(req.subdomains);
        req._subdomainLevel = req._subdomainLevel || 0;

        let subdomains = subdomain.split('.');
        let length = subdomains.length;
        let match = true;

        for(let i = 0; i < length; i++) {
             let expect = subdomains[length-(i+1)];
             let actual = req.subdomains[req._subdomainLevel+i];

             if(expect === '*') {
                 continue;
             }

             if(actual !== expect) {
                 match = false;
                 break;
             }
        }
        if(match) {
            console.log('match');
            req._subdomainLevel++;
            return fn(req, res, next)
        }
        next()
    };
}