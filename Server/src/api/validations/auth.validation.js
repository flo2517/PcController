const validateEmail = (email) => {
    return String(email).match(/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b/i);
};

const validatePassword = (password) => {
    return String(password).match(/^(?=.[a-z])(?=.[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/i);
};

module.exports = {
    validateEmail,
    validatePassword
}