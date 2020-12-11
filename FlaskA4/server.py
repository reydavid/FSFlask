'''
Create a new Flask project and create.
Create a server.py file that contains all of the code to get your server up and running. In the server.py file create the following the routes: 
/display-name this will render a template that displays your name in h1 tags
/display-food this will render a template that displays your favorite food in h1 tags including an image of that food.
/display-vacation this will render a template that displays your favorite vacation destination in h1 tags including an image of that destination
'''

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/display-name')

def displayName():
    return render_template('name.html')

@app.route('/display-food')

def displayFood():
    return render_template('food.html')

@app.route('/display-vacation')

def displayVacation():
    return render_template('vacation.html')



if __name__ == '__main__':
        app.run(debug = True)