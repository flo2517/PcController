const validateEmail = (email) => {
    return String(email).match(/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b/i);
};

const validatePassword = (password) => {
    return String(password).match(/^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$/i);
};

module.exports = {
    validateEmail,
    validatePassword
}