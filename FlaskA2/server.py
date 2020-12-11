from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/add-data', methods = ['POST'])

def displayData():
    firstname = request.form['f-name']
    lastname = request.form['l-name']
    email = request.form['email']
    favorite_food = request.form['favorite_food']
    
    return render_template("display.html", firstname = firstname, lastname = lastname, email = email, favorite_food = favorite_food)


if __name__ == '__main__':
        app.run(debug = True)