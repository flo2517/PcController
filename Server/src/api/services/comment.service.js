
const Sequelize = require('sequelize');
const {Comment} = require("../models/index");

class CommentService {
    constructor() {
        this.comment = Comment;
    }



    async getComments(limit, offset) {
        return this.comment.findAndCountAll(
            {
                order: [
                    ['createdAt', 'DESC']
                ],
                limit,
                offset
            }
        );
    }

    async averageRating() {
        return this.comment.findAll({
            attributes: [
                [Sequelize.fn('AVG', Sequelize.col('note')), 'averageRating']
            ]
        });
    }

    async addComment(comment) {
        return this.comment.create(comment);
    }
    
}

module.exports = CommentService;