from flask import Flask,render_template
import random



# def make_h1(func):
#     def wrapper(*args,**kwargs):
#         half_ans=func(*args,**kwargs)
#         ans= "<h1>"+half_ans+"</h1>"
#         return ans
#     return wrapper

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("indexhome.html")


@app.route("/movie")
def movie():
    return render_template("movie.html")


@app.route("/profile")
def profile():
    return render_template("index.html")


@app.route('/me')
def me():
    return render_template("me.html")


if __name__=="__main__":
    rand=random.randint(0,10)
    app.run(debug=True)