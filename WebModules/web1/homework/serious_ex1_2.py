from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1> Serious Excercise 1 by Tuan Anh</h1><br>Enter your BMI thru this link: http://127.0.0.1:5000/BMI/'/(insert weight)/(insert height)in centimeters"

@app.route("/bmi/<int:weight>/<int:height>(in centimeter)")
def BMI(weight, height):
    return render_template("BMI.html")

if __name__ == "__main__":
    app.run(debug = True)