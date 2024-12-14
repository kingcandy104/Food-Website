from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/foodfact')
def foodfact():
    return render_template("foodfact.html")
@app.route('/recipie')
def recipie():
    return render_template("recipie.html")
if __name__ == '__main__':
    app.run(debug = True, port = 5001)