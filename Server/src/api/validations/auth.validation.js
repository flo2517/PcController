const validateEmail = (email) => {
    return String(email).match(/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b/i);
};

const validatePassword = (password) => {
    return String(password).match(/^(?=.*?[A-Z])(?=(.*[a-z])+)(?=(.*[\d])+)(?=(.*[\W])+)(?!.*\s).{8,}$/igm);
};

module.exports = {
    validateEmail,
    validatePassword
}