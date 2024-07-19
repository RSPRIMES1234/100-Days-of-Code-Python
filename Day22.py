from turtle import Turtle, Screen
import time

# Initialize game variables
a = "1"  # Ball direction indicator
speed = 0.05  # Ball speed

# Initial positions for the sliders
CORDS_1 = [(-600, 340), (-600, 320), (-600, 300), (-600, 280), (-600, 260)]
CORDS_2 = [(600, -340), (600, -320), (600, -300), (600, -280), (600, -260)]

# Text properties for the score display
FONT = ('Minecrafter', 50, 'normal')
ALLIGNMENT = 'center'

# Function to handle scoring and ball reset
def scorring(ball, p1_score, p2_score):
    global speed
    if ball.xcor() > 660:  # Player 1 scores
        p1_score.score += 1
        speed = 0.05  # Reset speed
        ball.reset1()
        return False
    elif ball.xcor() < -660:  # Player 2 scores
        p2_score.score += 1
        speed = 0.05  # Reset speed
        ball.reset2()
        return False
    else:
        return True

# Function to determine the ball's movement mode
def mode(ball, slider1, slider2):
    global a
    global speed

    scorring(ball, p1_score, p2_score)
    xx = ball.xcor()
    yy = ball.ycor()

    # Ball movement logic based on its position
    if 300 > yy and (a == "1" or a == "7"):
        a = "1"
    elif 300 < yy and a == "1":
        a = "2"
    elif -300 > yy and a == "3":
        a = "4"
    elif 300 < yy and a == "4":
        a = "5"

    # Collision with sliders logic
    if slider2.xcor() == xx and a == "2" and abs(slider2.ycor() - yy) < 50:
        speed -= 0.005
        a = "3"
    if slider1.xcor() == xx and a == "5" and abs(slider1.ycor() - yy) < 50:
        speed -= 0.005
        a = "6"
    elif -300 > yy and a == "6":
        a = "7"

# Class for the ball
class Ball(Turtle):
    global a
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()

    # Reset ball position when Player 1 scores
    def reset1(self):
        global a
        self.goto(0, 0)
        a = "3"
        self.start_move()

    # Reset ball position when Player 2 scores
    def reset2(self):
        global a
        self.goto(0, 0)
        a = "1"
        self.start_move()

    # Start ball movement based on current mode
    def start_move(self):
        global a
        xx = self.xcor()
        yy = self.ycor()
        if a == "1":
            self.goto(xx + 10, yy + 10)
            time.sleep(speed)
        elif a == "2":
            self.goto(xx + 10, yy - 10)
            time.sleep(speed)
        elif a == "3":
            self.goto(xx - 10, yy - 10)
            time.sleep(speed)
        elif a == "4":
            self.goto(xx - 10, yy + 10)
            time.sleep(speed)
        elif a == "5":
            self.goto(xx - 10, yy - 10)
            time.sleep(speed)
        elif a == "6":
            self.goto(xx + 10, yy - 10)
            time.sleep(speed)
        elif a == "7":
            self.goto(xx + 10, yy + 10)
            time.sleep(speed)

# Function to check if sliders are within bounds
def notout(slider):
    if slider.distance(-600, 300) < 15 or slider.distance(-600, -300) < 15 or slider.distance(600, 300) < 15 or slider.distance(600, -300) < 15:
        return False
    else:
        return True

# Class for the sliders (paddles)
class sliders(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.cords = cords
        self.shape("square")
        self.color("white")
        self.pencolor("white")
        self.speed("fastest")
        self.shapesize(stretch_len=5)
        self.left(90)
        self.penup()
        self.goto(self.cords)

    # Move slider down
    def downn(self):
        y_cor = self.ycor() - 40
        self.goto(self.xcor(), y_cor)

    # Move slider up
    def upp(self):
        y_cor = self.ycor() + 40
        self.goto(self.xcor(), y_cor)

# Class to handle score display
class scorewriter(Turtle):
    def __init__(self, cordi):
        self.score = 0
        self.cordi = cordi
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(self.cordi)
        self.pendown()
        self.pencolor("White")
        self.writeu()

    # Function to display the score
    def writeu(self):
        self.message = f"{self.score}"
        self.clear()
        self.write(self.message, font=FONT, align=ALLIGNMENT)

    # Update the score
    def updatee(self):
        self.score += 1
        self.message = f"{self.score}"
        self.writeu()

# Set up the screen
sc = Screen()
sc.setup(1280, 720)
sc.bgcolor("black")
sc.title("PingPong Game")
sc.tracer(0)

# Initialize scores
p1_score = scorewriter((-70, 280))
p2_score = scorewriter((70, 280))

# Draw middle line
middle_line = Turtle()
middle_line.pencolor("white")
middle_line.hideturtle()
middle_line.penup()
middle_line.goto(0, 360)
middle_line.right(90)
for _ in range(36):
    middle_line.pendown()
    middle_line.forward(20)
    middle_line.penup()
    middle_line.forward(20)

# Create sliders and ball
slider_1 = sliders((-600, 300))
slider_2 = sliders((600, -300))
ball = Ball()

# Main game loop
while True:
    p1_score.writeu()
    p2_score.writeu()
    sc.update()

    sc.listen()
    ball.start_move()
    sc.onkey(slider_1.downn, "s")
    sc.onkey(slider_1.upp, "w")
    sc.onkey(slider_2.downn, "Down")
    sc.onkey(slider_2.upp, "Up")
    mode(ball, slider_1, slider_2)

# Keep the screen open
sc.mainloop()
