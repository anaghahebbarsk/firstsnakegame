from turtle import Turtle

class Score_board(Turtle):

    def __init(self):
        super().__init__(self)
        self.score = 0
        self.color("blue")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", True, align='centre', font=('Arial', 8, 'normal'))


