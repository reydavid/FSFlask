'''
    1. Create an app that takes in your first name, last name, username, e-mail and a password via form submission.
    2. Save that data to your database
    3. This app must then redirect to a new page
       Display your form data on this new page.


    1. Use Flask Assignment 1 to build out this assignment.
    2. Add a login field to your app that searches your database for the correct username and password.
    3. If the correct user name and password is found re-route the user to a page that displays the the message "Welcome {{USERNAME}}"

'''


from flask import Flask, render_template, request, redirect, session

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)

app.secret_key = 'mks'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///name_of_db.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200), nullable = False)
    pwd = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

@app.route('/')

def index():
    return render_template('index.html')

@app.route("/add-user", methods = ['GET','POST'])

def addToDB():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['pwd']

        register_user = User(
            username=username,
            pwd=pwd
        )

        db.session.add(register_user)

        db.session.commit()
            
        return render_template("display.html", user = register_user)
    
    else:

        return render_template('register.html')

@app.route('/login-user', methods=['POST'])

def login():
    username = request.form['username']
    password = request.form['pwd']

    user = User.query.filter_by(username = username, pwd = password).first()

    if user is not None:
        return render_template("display.html", username = username)
    else:
        return redirect('/')

if __name__ == "__main__":
    db.create_all()

    app.run(debug = True)