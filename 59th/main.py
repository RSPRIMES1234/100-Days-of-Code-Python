from flask import Flask,render_template,request
import requests
import smtplib

app=Flask(__name__)

admin_email="ujioppujiopjio'"

to_email="gilyuyuyu"
password="huiolyuiooyhi;o;yhi"

@app.route("/")
def home():
    blogs=requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
    return render_template("index.html",page="home",blogs=blogs)

@app.route("/about")
def about():
    return render_template("about.html",page="about")


@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method =="GET":
        return render_template("contact.html",page="contact")
    elif request.method =="POST":
        name= request.form['name']
        email=request.form['email']
        phone = request.form['phone']
        message=request.form['message']
        print(name,email,phone,message)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=admin_email, password=password)
            print(f"Name:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}")
            connection.sendmail(admin_email,to_email,f"Subject:New Message\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}")

        return render_template("contact.html", page="success")


@app.route("/post/int:<id>")
def post(id):
    blog = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()[int(id)-1]
    return render_template("post.html",blog=blog)




if __name__=="__main__":
    app.run(debug=True)