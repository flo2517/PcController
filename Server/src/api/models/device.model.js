import sequelize from "../../config/db.config";

const Device = sequelize.define("device", {
  id: {
    type: sequelize.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
    uuid: {
        type: sequelize.STRING(255),
        allowNull: false,
        unique: true
    },
  name: {
    type: sequelize.STRING(255),
    allowNull: false
  }
});