#setup server 

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # neu nguoi dung truy cap vao trang chu thi gọi hàm dưới đây
def homepage():
    return "WEEEEEEEEEEEEEEEEEEEEEEEE"

@app.route("/praise/shit")
def praise_shit():
    return "shit is awesome"

@app.route("/praise/<name>")
def praise(name):
    return name + ' is superb'

@app.route("/add/<int:int1>/<int:int2>")
def add(int1, int2):
    total = int1 + int2 * 2
    return str(total)

@app.route("/question")
def show_question():
    return render_template("question.html")


if __name__ == "__main__":
    app.run(debug = True)

