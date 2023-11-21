import mysql.connector as mysql
from tabulate import tabulate
from flask import Flask, render_template, request

app = Flask(__name__)
HOST = 'localhost'
DATABASE = 'appTest1'
USER = 'app1.0.0'
PASSWORD = ''

db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
cursor = db_connection.cursor()
print('connected to database')

@app.route("/", methods=['POST' ,'GET'])
def index():
    if request.method == 'POST':
        user_details = []
        username = request.form['username']
        password = request.form['password']

        def add_to_list(user_details):
            user_details.append(username)
            user_details.append(password)
        add_to_list(user_details)
        print(user_details)
        
        sql_statment = "SELECT EXISTS (SELECT * FROM users WHERE username=%s and password=%s);"
        cursor.execute(sql_statment,user_details)
        result= cursor.fetchall()
        print(result)
        feedback= result[0]
    if str(feedback) == '(1,)' :
        print('access granted')
    else:
        print('access denied')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
