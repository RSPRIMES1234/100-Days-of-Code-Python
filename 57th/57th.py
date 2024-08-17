from flask import Flask,render_template
import datetime as dt
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html",year=dt.date.today().year)

@app.route("/guess/<name>")
def guess(name):
    name=name.capitalize()
    GENDER_LINK = f"https://api.genderize.io?name={name}"
    AGE_LINK = f"https://api.agify.io?name={name}"
    gen=requests.get(url=GENDER_LINK)
    gender=gen.json()["gender"]
    agee=requests.get(url=AGE_LINK)
    age=agee.json()["age"]

    return render_template("age_gender.html",age=age,gender=gender,name=name)


@app.route("/blog")
def blog():
    blogs=requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blogs.raise_for_status()
    blogs=blogs.json()
    print(blogs)
    return render_template("blog.html",blogs=blogs)


if __name__=="__main__":
    app.run(debug=True)