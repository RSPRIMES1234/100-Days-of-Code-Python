from flask import request,Flask,render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = EmailField(label='Email',validators=[DataRequired()])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8, max=20)])
    submit=SubmitField(label="Log In")

app=Flask(__name__)
app.secret_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@email.com" and form.password.data=="12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html",form=form)






if __name__=="__main__":
    app.run(debug=True, port=5001)