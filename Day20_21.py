from turtle import Turtle,Screen
import time
import random

CORDS= [(0, 0), (-20, 0), (-40, 0)]
FONT=('monaco', 10, 'bold')
ALLIGNMENT='left'


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.random_spawn()

    def random_spawn(self):
            lox=random.randint(-280,280)
            loy=random.randint(-280,280)
            self.goto(lox,loy)




class Snake:

    def __init__(self):
        self.turtuls = []
        self.create_snake()

        self.head = self.turtuls[0]
    def create_snake(self):
        for pos in CORDS:
            self.create(pos)

    def create(self,pos):
        new_turtul=Turtle("square")
        new_turtul.color("white")
        new_turtul.penup()
        new_turtul.speed("fastest")
        new_turtul.goto(pos)
        self.turtuls.append(new_turtul)
    def longer(self):
        self.create(self.turtuls[-1].position())

    def move(self):
            i = 0
            x=len(self.turtuls)
            while i < x - 1:
                self.turtuls[x-1-i].goto(self.turtuls[x- 2- i].pos())
                i += 1
            self.turtuls[0].forward(20)

    def snake_up(self):
        head=self.head
        heading=head.heading()
        if heading==0 or heading==180:
            head.setheading(90)
        else:
            pass

    def snake_left(self):
        head=self.head
        heading = head.heading()
        if heading==90 or heading==270:
            head.setheading(180)
        else:
            pass

    def snake_right(self):
        head=self.head
        heading = head.heading()
        if heading==90 or heading==270:
            head.setheading(0)
        else:
            pass

    def snake_down(self):
        head=self.head
        heading = head.heading()
        if heading==180 or heading==0:
            head.setheading(270)
        else:
            pass


class scorewriter(Turtle):

    def __init__(self):
        self.score=0
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-40,280)
        self.pendown()
        self.pencolor("White")
        self.message=f"Score : {self.score}"
        self.writeu()

    def writeu(self):
        self.clear()
        self.write(self.message, font=FONT ,align=ALLIGNMENT )
    def updatee(self):

        self.score+=1
        self.message = f"Score : {self.score}"
        self.writeu()

def check_gameover():
    head_pos=snake.head.pos()
    while -290<head_pos[0]<290  and -290<head_pos[1]<290 :
        return True
    return False



sc=Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)
snake=Snake()
food=Food()
sc.listen()

score_writer=scorewriter()


sc.onkey(snake.snake_up, "Up")
sc.onkey(snake.snake_down, "Down")
sc.onkey(snake.snake_left, "Left")
sc.onkey(snake.snake_right, "Right")


game_is_on=check_gameover()
while game_is_on:
    game_is_on = check_gameover()
    sc.listen()

    sc.onkey(snake.snake_up, "Up")
    sc.onkey(snake.snake_down, "Down")
    sc.onkey(snake.snake_left, "Left")
    sc.onkey(snake.snake_right, "Right")
    sc.update()
    time.sleep(0.05)
    snake.move()


    if snake.head.distance(food)<15:
        food.random_spawn()
        score_writer.updatee()
        snake.longer()
    for _ in snake.turtuls[1:]:
        if snake.head.distance(_)<15:
            game_is_on=False

game_over=Turtle()
game_over.pencolor("White")
game_over.hideturtle()
game_over.speed("fastest")
game_over.write("GameOver",font=FONT,align='center')
sc.update()


sc.mainloop()
