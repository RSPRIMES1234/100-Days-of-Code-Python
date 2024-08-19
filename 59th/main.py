from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route("/")
def home():
    blogs=requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
    return render_template("index.html",page="home",blogs=blogs)

@app.route("/about")
def about():
    return render_template("about.html",page="about")


@app.route("/contact")
def contact():
    return render_template("contact.html",page="contact")

@app.route("/post/int:<id>")
def post(id):
    blog = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()[int(id)-1]
    return render_template("post.html",blog=blog)


if __name__=="__main__":
    app.run(debug=True)