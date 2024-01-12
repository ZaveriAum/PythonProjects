from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")

    def refresh(self):
        xcor = random.randint(-260, 260)
        ycor = random.randint(-260, 260)
        self.goto(xcor, ycor)

