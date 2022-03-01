const validateEmail = (email) => {
    //return String(email).match(/^(?=.[a-z])(?=.[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/i);
    return true;
};

const validatePassword = (password) => {
    // return String(password).match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/);
    return password.length >= 8;
};

module.exports = {
    validateEmail,
    validatePassword
}