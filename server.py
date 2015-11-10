from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'wordsAndStuffandThings'
mysql = MySQLConnector('friendsdb')

#---------------------------------------
# INDEX DONE 
@app.route('/')
def index():
    friends = mysql.fetch("SELECT * FROM friends")
    return render_template('index.html', friends=friends)

# CREATE DONE
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
    # print query
    mysql.run_mysql_query(query)
    return redirect('/')

#---------------------------------------

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):

	# function goes here 
	return edit

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	# function goes here
	return update

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	# DELETE * from where id =
	# function goes here
	return destroy

app.run(debug=True)