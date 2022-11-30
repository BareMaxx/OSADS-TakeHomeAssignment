from flask import Flask
from flask import request
import json
import mysql.connector as mysql

app = Flask(__name__)

database = mysql.connect(
	host = "databaseBackendNetwork",
	username = 'root',
	password = "test",
	database = "personsdatabase",
	port = "3306"
)

@app.route("/person", methods = ["POST"])
def person():
	cursor = database.cursor()
	firstName = request.form["firstname"]
	lastName = request.form["lastname"]
	stm = """INSERT INTO person (Firstname, Lastname) VALUES (%s, %s)"""
	val = (firstName, lastName)
	cursor.execute(stm, val)
	database.commit()
	return ("", 200)
	
@app.route("/persons")
def persons():
	cursor = database.cursor(dictionary = True)
	stm = """SELECT * FROM person"""
	cursor.execute(stm)
	response = json.dumps(cursor.fetchall())
	return (response,200)

if __name__ == '__main__':
    app.run(host="0.0.0.0")