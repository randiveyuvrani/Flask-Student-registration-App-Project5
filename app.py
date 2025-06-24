from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
app.config.from_object(config)

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO students (name, email, phone, course, address) VALUES (%s, %s, %s, %s, %s)",
                (name, email, phone, course, address))
    mysql.connection.commit()
    cur.close()
    return "✅ Student registered successfully!"

@app.route('/students')
def students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return render_template('students.html', students=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

