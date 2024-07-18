#Drawing Book

# from turtle import Turtle,Screen
#
# turtul=Turtle()
# sc=Screen()
# sc.title("Drawing Book")
# sc.setup(width = 1.0, height = 1.0)
# FONT = ("Arial", 20, "bold")
# turtul.pensize(3)
#
# def clear_screen():
#     turtul.clear()
# def ahead():
#     turtul.forward(20)
# def left_turn():
#     turtul.left(20)
# def right_turn():
#     turtul.right(20)
# def back():
#     turtul.back(20)
# def change_colour():
#     color_name=sc.textinput("Change Colour","entre the color name")
#     turtul.pencolor(color_name)
#     sc.listen()
# turtul.write("""This is a Drawing Book you can certains things that are mentaioned below:
# 1. Move Forward : 'w'
# 2.Move Backward : 's'
# 3.Turn Left : 'a'
# 4.Turn Right : 's'
# 5.Change Pen Colour : 'c'
# 6.Reset Screen : 'x'
#
# PRESS 'X' to continue
# """,font=FONT,align="center")
# sc.listen()
#
# sc.onkey(key="w",fun=ahead)
# sc.onkey(key="a",fun=left_turn)
# sc.onkey(key="d",fun=right_turn)
# sc.onkey(key="s",fun=back)
# sc.onkey(key="c",fun=change_colour)
# sc.onkey(key="x",fun=clear_screen)
#
#
#
# sc.mainloop()






#Turtle race game

import random


def random_speed():
    sp=random.randint(5,30)
    return sp
from turtle import Turtle,Screen

sc=Screen()
sc.title("Turtle Race Game")
sc.setup(width = 800, height = 800)

# turtle0=Turtle()
# turtle0.penup()
# turtle0.goto(390,390)
# turtle0.right(90)
# turtle0.pendown()
# turtle0.forward(800)
# turtle0.penup()


turtle1=Turtle()
turtle1.penup()
turtle1.color("red")
turtle1.shape("turtle")


turtle2=Turtle()
turtle2.penup()
turtle2.color("blue")
turtle2.shape("turtle")


turtle3=Turtle()
turtle3.penup()
turtle3.color("green")
turtle3.shape("turtle")


turtle4=Turtle()
turtle4.penup()
turtle4.color("purple")
turtle4.shape("turtle")

turtle5=Turtle()
turtle5.penup()
turtle5.color("yellow")
turtle5.shape("turtle")


user_choice=sc.textinput("Turtle choice","Choose which colour turtle will win red,green,blue,purple or yellow")
user_choice=user_choice.lower()


turtle1.goto(-350,300)
turtle2.goto(-350,150)
turtle3.goto(-350,0)
turtle4.goto(-350,-150)
turtle5.goto(-350,-300)
winner=""
for _ in range(100):
    if turtle1.pos()[0]>=370:
        winner="red"
        break
    elif turtle2.pos()[0]>=370:
        winner="blue"
        break
    elif turtle3.pos()[0]>=370:
        winner="green"
        break
    elif turtle4.pos()[0]>=370:
        winner="purple"
        break
    elif turtle5.pos()[0]>=370:
        winner="yellow"
        break
    x=random_speed()
    turtle1.forward(x)
    x=random_speed()
    turtle2.forward(x)
    x=random_speed()
    turtle3.forward(x)
    x=random_speed()
    turtle4.forward(x)
    x=random_speed()
    turtle5.forward(x)

if user_choice==winner:
    print(f"You won {winner} won the race !")
else :
    print(f"You lost {winner} won the race !")
sc.mainloop()
