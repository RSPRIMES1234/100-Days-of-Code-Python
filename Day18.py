import colorgram
from turtle import Turtle
import random
import turtle as t

turn=[0,1]




colors=colors = colorgram.extract('img_1.png', 6)
def random_tuple():
    l = colorgram.extract("img_1.png", 20)
    return random.choice(l)
def random_turn(turtul):
    a=random.choice(turn)
    if a==0:
        turtul.left(90)
    else:
        turtul.right(90)
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtul.color(R, G, B)

turtul=Turtle()

turtul.speed("fastest")
turtul.pensize(2)

t.colormode(255)

# for _ in range(4):
#     turtul.forward(100)
#     turtul.left()



# for _ in range(50):
#     turtul.forward(5)
#     turtul.penup()
#     turtul.forward(5)
#     turtul.pendown()



# i = 3
# angle=120
#
# while i<11:
#
#     change_color()
#
#     for _ in range(i):
#         turtul.forward(100)
#         turtul.right(angle)
#     i+=1
#     angle=360/i
#     print(i,angle)




# for _ in range(100):
#     turtul.forward(15)
#     random_turn(turtul)
#     change_color()

# for _ in range(72):
#     turtul.circle(150)
#     change_color()
#     turtul.left(5)


turtul.ht()
turtul.penup()
a = turtul.position()
print(a)
b=0

for _ in range(10):


    for _ in range(10):
        a=random_tuple()
        color=(a.rgb.r,a.rgb.g,a.rgb.b)
        turtul.dot(10,color)
        turtul.forward(20)

    b+=20
    turtul.setposition((0,b))

turtul.screen.mainloop()
