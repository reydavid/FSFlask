from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.secret_key = "secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FSFlaskA4.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

@app.route('/')
@app.route('/showUser', methods = ['GET'])
@app.route('/editUser', methods = ['POST','GET'])

def index():
    allUsers = User.query.all()
    return render_template("users.html", allUsers = allUsers)

@app.route('/adduser', methods = ['POST','GET'])
@app.route('/new', methods = ['POST'])

def addUser():

    if request.method == 'POST':
        firstName = request.form['first_name']
        lastName = request.form['last_name']
        email = request.form['email']

        new_User = User(first_name = firstName, last_name = lastName, email= email)

        db.session.add(new_User)

        db.session.commit()

        return redirect('/')

    else:
     
        return render_template('new.html')

@app.route('/remove/<int:user_id>')

def removeUser(user_id):
    rmvd_user = User.query.filter_by(id = user_id).first()
    
    db.session.delete(rmvd_user)

    db.session.commit()

    return redirect('/')



if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)