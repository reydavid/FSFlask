from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.secret_key = "secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FSFlaskA3.db'

db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(400),nullable=False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

@app.route('/')

def index():
    allCourses = Course.query.all()
    return render_template("index.html", allCourses = allCourses)

@app.route('/addcourse', methods = ['POST'])

def addCourse():
#if without else?

    if request.method == 'POST':
        name = request.form['course_name']
        description = request.form['course_description']

        new_course = Course(name = name, description= description)

        db.session.add(new_course)

        db.session.commit()

    return redirect('/')

@app.route('/remove/<int:course_id>')
#/remove/<int: comes up with a type error, missing a closing ">"

def removeCourse(course_id):
    #initial course_id parameter problem. what is this reference?
    rmv_course = Course.query.filter_by(id = course_id).first()
    
    db.session.delete(rmv_course)

    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)