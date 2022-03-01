const Sequelize = require('sequelize');
const {User} = require("../models/index");

class UserService {

  constructor() {}

  async getUser(id) {
    return User.findAll({
      where: {
        id: id,
      },
    });
  }

  async getUserByEmail(email) {
    return User.findAll({
      where: {
        email: email,
      },
    });
  }

  async getUserByVerifyString(verifyString) {
    return User.findAll({
      where: {
        verifyString: verifyString,
      },
    });
  }

  async getUsers() {
    return User.findAll();
  }

  async createUser(user) {
    return User.create(user);
  }

  async updateUser(id, user) {
    return User.update({
      name: user.name,
      email: user.email,
      password: user.password,
    }, {
      where: {
        id: id,
      },
    });
  }

  async deleteUser(id) {
    return User.destroy({
      where: {
        id: id,
      },
    });
  }

  async getUserByResetPasswordToken(resetPasswordToken) {
    return User.findAll({
      where: {
        resetPasswordToken: resetPasswordToken,
      },
    });
  }
}

module.exports = UserService;