import random
from turtle import Turtle
import random


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.is_game_on = True
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.width = 20
        self.height = 20
        self.setheading(75)
        self.right(random.random() * 40)
        self.each_step = 0.1

    def pong_move(self):
        self.speed("slow")
        self.forward(self.each_step)
        self.bounce_wall()

    def bounce(self):
        self.setheading(360 - self.heading())

    def bounce_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.bounce()

    def reset_position_player1(self):
        self.goto(0, 0)
        self.setheading(115)
        self.left(random.random() * 40)

    def reset_position_player2(self):
        self.goto(0, 0)
        self.setheading(75)
        self.right(random.random() * 40)

    def increase_speed(self):
        self.each_step += 0.1

    def reset_speed(self):
        self.each_step = 0.1