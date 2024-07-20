from turtle import Turtle,Screen
import time
import random
i=0
X=10
FONT=('Minecrafter', 15, 'normal')
ALLIGNMENT='center'
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def finish(self):
        if self.distance((0,280))<1:
            return True
        else:
            return False
    def reset(self):
        self.goto(STARTING_POSITION)



class CarManager:
    def __init__(self):
        self.carlist=[]
        self.increments=MOVE_INCREMENT
    def create_car(self):
        car=Turtle()
        car.shape('square')
        car.shapesize(stretch_len=3,stretch_wid=1.5)
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.penup()
        car.goto(300,random.randint(-220,220))
        self.carlist.append(car)
    def load_cars(self):
            global i
            a=random.randint(0,6)
            for _ in range(a):
                self.create_car()
            i=0
    def move(self):
        for _ in self.carlist:
            _.forward(MOVE_DISTANCE)
            time.sleep(0.009)


    def car_colision(self,player):
        for _ in self.carlist:
            if player.distance(_.pos())<30:
                return True
            else:
                False





class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.goto(-200,250)

    def writt(self):
        self.clear()
        self.write(f"Level : {self.level}",font=FONT,align=ALLIGNMENT)
    def score_update(self):
        self.level+=1
        self.writt()
    def gameover(self):
        self.goto(0,0)
        self.clear()
        self.write("GameOver", font=FONT, align=ALLIGNMENT)

sc = Screen()
sc.setup(width=600, height=600)
sc.tracer(0)
player=Player()
score=Scoreboard()
game_is_on = True
car_manager=CarManager()
car_manager.load_cars()

while game_is_on:
    if i == X:
        car_manager.load_cars()
    finish=player.finish()
    collision=car_manager.car_colision(player)
    if collision :
        score.gameover()
        game_is_on=False
    elif not finish :

        car_manager.move()
        score.writt()
        sc.listen()
        sc.onkey(player.move,"w")
        time.sleep(0.001)
        sc.update()

    else:
        player.reset()
        score.score_update()
        MOVE_DISTANCE+=MOVE_INCREMENT
        X-=1
    i+=1

sc.mainloop()
