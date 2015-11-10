from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# app.secret_key = 'wordsAndStuffandThings' *ONLY REQ FOR SESSIONS*
mysql = MySQLConnector('friendsdb')

@app.route('/')
def index():
    friends = mysql.fetch("SELECT * FROM friends")
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
    # print query
    mysql.run_mysql_query(query)
    return redirect('/')

@app.route('/friends/<int:id>/edit', methods=['GET']) #int: not necessary, but good to know
def edit(id):
	friend = mysql.fetch("SELECT * FROM friends where id = {}".format(id))
	if friend:
		return render_template('edit.html', friends = friend)
	return redirect('/friends/'+str(id))
	# return edit

@app.route('/friends/<int:id>/update', methods=['POST']) #int: not necessary, but good to know
def update(id):
	query = "UPDATE friends SET first_name='{}', last_name='{}', occupation='{}' WHERE id='{}'".format(request.form['first_name'], request.form['last_name'], request.form['occupation'],id)
	# print query
	mysql.run_mysql_query(query)
	return redirect('/')
	# return update

@app.route('/friends/<int:id>/delete', methods = ['POST']) #int: not necessary, but good to know
def delete(id):
	friend = mysql.fetch("SELECT * FROM friends where id ={}".format(id))
	query = "DELETE FROM friendsdb.friends WHERE id={}".format(id)
	mysql.run_mysql_query(query)
	return redirect('/')

app.run(debug=True)



































































