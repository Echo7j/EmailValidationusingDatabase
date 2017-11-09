from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector


import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ThisisSecret"
mysql = MySQLConnector(app,'friendsdb')

@app.route ('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():



	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is incorrect")
		return redirect ('/')
	else:
		query = "INSERT INTO emails (email,created_at) VALUES(:email,NOW())"
		data = {
				'email':request.form['email']
		}
		# for id in query:
		# 	if query.email.attr == data.val: 
		# 		flash ("Email already exist in database")
		# 		return redirect ('/')
		mysql.query_db(query,data)
		flash("Email adde")
		return redirect('/success')

@app.route('/success')
def results():
	query = "SELECT * FROM emails"
	emails = mysql.query_db(query)
	print emails
	return render_template ('success.html', all_emails = emails)



app.run(debug=True)