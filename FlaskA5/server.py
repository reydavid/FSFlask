from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'mks'

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/add-data', methods = ['POST','GET'])

def displayData():
    if request.method == 'POST':
        session["fname"] = request.form['first_name']
        session["lname"] = request.form['last_name']
        session["eml"] = request.form['email']
        session["favfood"] = request.form['favorite_food']
        
        
        """ firstname = request.form['first_name']
        lastname = request.form['last_name']
        email = request.form['email']
        favorite_food = request.form['favorite_food'] """
        
        return render_template("display.html")

        """ return render_template("display.html", firstname = firstname, lastname = lastname, email = email, favorite_food = favorite_food) """

    else:
        return redirect('/')

if __name__ == '__main__':
        app.run(debug = True)