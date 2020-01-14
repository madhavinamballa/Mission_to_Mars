# import necessary libraries
from flask import Flask, render_template
# create instance of Flask app
app = Flask(__name__)
# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("test.html")
@app.route("/scarpe")
def bonus():

    return render_template("test.html")
if __name__ == "__main__":
    app.run(debug=True)
