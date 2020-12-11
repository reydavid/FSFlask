from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/add-data', methods = ['POST'])

def addData():
    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        gender = request.form['gender']
    
        return render_template("display.html", first_name = first_name, last_name = last_name, email = email, address=address, city = city, state = state, zip_code = zip_code, gender = gender)
    return redirect('/')

if __name__ == '__main__':
        app.run(debug = True)