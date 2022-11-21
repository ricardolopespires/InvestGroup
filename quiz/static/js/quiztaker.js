

const Sequelize = require('sequelize');
const database = require('./db');


const QuizTaker = database.define('quiztaker',{
	
	id:{
		type:Sequelize.INTEGER,
		autoIncrement:true,
		allowNull:false,
		primaryKey:true
	},

	user:Sequelize.INTEGER, 
    quiz:Sequelize.STRING,
    score:Sequelize.INTEGER,
    completed:Sequelize.BOOLEAN,
    date_finished:Sequelize.DATE,
    timestamp:Sequelize.FLOAT,

}) 


console.log(QuizTaker)

module.exports = QuizTaker;