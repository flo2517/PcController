const {sequelize} = require("../../config/db.config");
const {Sequelize, Model} = require("sequelize");


class Comment extends Model {
}

Comment.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        primaryKey: true
    },
    username: {
        type: Sequelize.STRING,
        allowNull: false
    },
    note: {
        type: Sequelize.INTEGER,
        allowNull: false
    },
    comment: {
        type: Sequelize.STRING,
        allowNull: false
    }
}, {
    sequelize,
    modelName: 'comment'
});

sequelize.define("comment", Comment.attributes, Comment.options);

module.exports = Comment;