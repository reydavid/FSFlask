from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')
'''
@app.route('display-movie')
    return render_template('movie.html', movie = "How to Train your Dragon", favorite_food = "Pho" )

@app.route('/display-artist')
    return render_template("artist.html")
'''





if __name__ == '__main__':
    app.run(debug = True)