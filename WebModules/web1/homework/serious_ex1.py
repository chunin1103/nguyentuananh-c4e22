from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1> Serious Excercise 1 by Tuan Anh</h1><br>Enter your BMI thru this link: http://127.0.0.1:5000/BMI/'/(insert weight)/(insert height)in centimeters"

@app.route("/bmi/<int:weight>/<int:height>(in centimeter)")
def BMI(weight, height):
    height = height / 100
    BMI = (weight / height) / height
    if BMI < 16:
        return('Severely Underweighted')
    elif 16 <= BMI <18.5:
        return('Underweight')
    elif 18.5 <= BMI <25:
        return('Normal')
    elif 25 <= BMI <30:
        return('Overweight')
    elif 30 < BMI:
        return('Obese man')
    else:
        return('r you not human ;)')

if __name__ == "__main__":
    app.run(debug = True)