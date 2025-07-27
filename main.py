from turtle import Screen,time
from scoreboard import Score_board
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score_board()

screen.listen()
screen.onkey(snake.go_up, key="Up")
screen.onkey(snake.go_down,key="Down")
screen.onkey(snake.go_right,key="Right")
screen.onkey(snake.go_left,key="Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect food eating
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
'''ef go_up():
    new_turtle.left(90.0)

def go_down():
    new_turtle.right(90.0)

def go_forward():
    new_turtle.forward(10)


def func():
    screen.onclick(key="Up",fun=go_up())
    screen.onclick(key="Down", fun=go_down())
    screen.onclick(key="Space", fun=go_forward()) ///


    if xcor(all[0]) == 300 or ycor(all[0]) == 300 or xcor(all[0]) == -300 or ycor(all[0]) == -300:
        print("foul!! Snake  hit the wall")
        break'''



