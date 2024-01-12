from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score = {self.score}. High Score: {self.high_score}", True, align="right",
                   font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()
