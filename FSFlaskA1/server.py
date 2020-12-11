'''
    1. Create an app that takes in your first name, last name, username, e-mail and a password via form submission.
    2. Save that data to your database
    3. This app must then redirect to a new page
       Display your form data on this new page.
'''


from flask import Flask, render_template, request, redirect, session

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)

app.secret_key = 'mks'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    fname = db.Column(db.String(200), nullable = False)
    lname = db.Column(db.String(200), nullable = False)
    username = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    pwd = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

@app.route('/')

def index():
    return render_template('index.html')

@app.route("/add-to-db", methods = ['POST'])

def addToDB():
    if request.method == 'POST':

        first_name = request.form['fname']
        last_name = request.form['lname']
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['pwd']

        new_user = User(
            fname=first_name,
            lname=last_name,
            username=username,
            email=email,
            pwd=pwd
        )

        db.session.add(new_user)

        db.session.commit()
            
        return render_template("display.html", user = new_user)
    
    else:

        return redirect('/')    

if __name__ == "__main__":
    db.create_all()

    app.run(debug = True)