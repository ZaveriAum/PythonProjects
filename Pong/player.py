from turtle import Turtle


class Player(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.xcor = xcor
        self.ycor = ycor
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.setx(self.xcor)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)
