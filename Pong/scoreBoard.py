from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.p1_sco = 0
        self.p2_sco = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p2_sco, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.p1_sco, align="center", font=("Courier", 80, "normal"))

    def p2_score(self):
        self.p2_sco += 1
        self.update_scoreboard()

    def p1_score(self):
        self.p1_sco += 1
        self.update_scoreboard()
