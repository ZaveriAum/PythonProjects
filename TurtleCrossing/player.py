from turtle import Turtle


class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -270)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def move_back(self):
        self.backward(20)

    def reset_position(self):
        if self.ycor() > 280:
            self.goto(0, -280)
            return True
