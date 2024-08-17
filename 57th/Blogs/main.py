from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blogs = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blogs.raise_for_status()
    blogs = blogs.json()
    print(blogs)
    return render_template("index.html", blogs=blogs)

@app.route("/post/int:<index>")
def blog_post(index):
    blogs=requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blogs.raise_for_status()
    blogs=blogs.json()
    print(blogs)
    return render_template("post.html",blog_num=int(index),blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)
