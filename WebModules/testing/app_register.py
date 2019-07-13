from flask import *
app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "GET":
    return render_template("register.html")
  elif request.method == "POST":
    form = request.form
    first_name = form['first_name']
    last_name  = form['last_name']
    yob        = form['yob']
    gender     = form['gender']
    city       = form['city']

    print(first_name, last_name, gender, yob, city)

    return "ok"
if __name__ == '__main__':
  app.run(debug=True)