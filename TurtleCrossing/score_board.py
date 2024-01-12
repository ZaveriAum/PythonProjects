from turtle import Turtle


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.level = 1
        self.write(f"Level {self.level}", align="center", font=("Arial", 15, "normal"))

    def increase_level(self):
        if self.level == 7:
            self.write("Game Over. You have won thank you for playing.\nGenji's turtle crossing.")
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="center", font=("Arial", 15, "normal"))
