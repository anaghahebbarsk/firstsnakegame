from turtle import Turtle, Screen, time

x_position = [-20, 0, 20]
move_distance = 20
up = 90
down = 270
right = 0
left = 180


class Snake:
    def __init__(self):
        self.all = []
        self.create_snake()
        self.head = self.all[0]

    def create_snake(self):
        for i in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(x=x_position[i], y=0)
            self.all.append(new_turtle)

    def move(self):
        for j in range(len(self.all) - 1, 0, -1):
            new_x = self.all[j - 1].xcor()
            new_y = self.all[j - 1].ycor()
            self.all[j].goto(new_x, new_y)
        self.head.forward(move_distance)

    def go_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def go_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def go_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def go_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)


'''screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)
all = []





game_is_on = True

ef go_up():
    new_turtle.left(90.0)

def go_down():
    new_turtle.right(90.0)

def go_forward():
    new_turtle.forward(10)


def func():
    screen.onclick(key="Up",fun=go_up())
    screen.onclick(key="Down", fun=go_down())
    screen.onclick(key="Space", fun=go_forward()) ///

while game_is_on:
    screen.update()
    time.sleep(0.1)



    if xcor(all[0]) == 300 or ycor(all[0]) == 300 or xcor(all[0]) == -300 or ycor(all[0]) == -300:
        print("foul!! Snake  hit the wall")
        break'''



