
const Sequelize = require('sequelize');
const User = require("../models/user.model");


class UserService {
  constructor() {

  }

  async getUser(id) {
    return User.findAll({
      where: {
        id: id,
      },
    });
  }

  async getUsers() {
    return User.findAll();
  }

  async createUser(user) {
    const newUser = await User.build(user, {
      isNewRecord: true,
      fields: ['username', 'email', 'password'],
    });
    console.log(newUser);
    return User.create(newUser);
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
}

module.exports = UserService;