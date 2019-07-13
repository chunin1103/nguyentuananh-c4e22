from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return '<h1> Welcome to Tuan Anh\'s homework page </h1> <a href="http://127.0.0.1:5000/about-me" target="_blank" rel="nofollow">About me</a>'

@app.route("/about-me")
def about_me():
    return render_template("aboutme.html")

@app.route("/school")

def school():
    return '''<meta http-equiv="refresh" content="0; URL='http://techkids.vn'" />'''

if __name__ == "__main__":
    app.run(debug = True)