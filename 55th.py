from flask import Flask
import random



def make_h1(func):
    def wrapper(*args,**kwargs):
        half_ans=func(*args,**kwargs)
        ans= "<h1>"+half_ans+"</h1>"
        return ans
    return wrapper

app = Flask(__name__)
#
# def make_bold(func):
#     def wrapper(*args,**kwargs):
#         half_ans=func(*args,**kwargs)
#         ans= "<b>"+half_ans+"</b>"
#         return ans
#     return wrapper
#
# def make_underlined(func):
#     def wrapper(*args,**kwargs):
#         half_ans=func(*args,**kwargs)
#         ans= "<u>"+half_ans+"</u>"
#         return ans
#     return wrapper
#
# def make_emphasis(func):
#     def wrapper(*args,**kwargs):
#         half_ans=func(*args,**kwargs)
#         ans= "<em>"+half_ans+"</em>"
#         return ans
#     return wrapper
#
# app = Flask(__name__)
#
# @app.route("/")
# @make_bold
# @make_underlined
# @make_emphasis
# def default():
#     return "Hi"

@app.route("/")
def hello():
    return f"<h1>Guess a Number between 0 and 10</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guess>")
def guesser(guess):
    if guess<rand:
        return "<h1 style=color:red>Too Low, Try Again</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExODJ6MGg3djdqbDlldzNoYmxsdmZ5d2JwdXozdzVueWl2djI1Z2F5ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif'>"
    elif guess > rand:
        return "<h1 style=color:red>Too High, Try Again</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDMycDkxNzduamt0b2JnMjNuNDhhMjAzOHZxM3FnaTN0ZmwweWtveSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7GUSNFWY0groElwc/giphy.gif'>"
    elif guess == rand:
        return "<h1 style=color:red>You are Correct!!</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWJsNDZtdTR4eGdraDgzNGhrdDkwOXd6bGU5MHhsMHp2ZzI0emR3byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3otPoS81loriI9sO8o/giphy.gif'>"



if __name__=="__main__":
    rand=random.randint(0,10)
    app.run(debug=True)


