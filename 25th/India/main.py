import turtle
import pandas as pd

a=pd.read_csv("gg3.csv")
sc=turtle.Screen()
sc.setup(800,963)
sc.bgpic("indian_state.png")
sc.title("Indian Quiz Game")

states=a["state"].tolist()
for _,value in enumerate(states):
    states[_]=value.lower()

xcords=a["x"].tolist()
ycords=a["y"].tolist()

answered=[]
gg=0
answer_left=29
right_answer=0
turtli=turtle.Turtle()
turtli.hideturtle()
turtli.penup()
def write_state():
    loc=states.index(input)
    states.pop(loc)
    xcord=xcords[loc]
    ycord=ycords[loc]
    turtli.goto(xcord,ycord)
    turtli.write(input)


while answer_left!=0 and gg<50:
    input=sc.textinput(f"{right_answer}/{answer_left}","Enter a state name")
    input=input.lower()
    if input in states:
        answer_left-=1
        right_answer+=1
        write_state()
    elif input=="exit":
        with open("Highscore.txt",'w') as filee:
            filee.write(str(right_answer))
            break
    gg+=1



if right_answer<29:
    print("Learn the below states")

    for _ in states:
        print(_)
elif right_answer==29:
    print("ggwp")


