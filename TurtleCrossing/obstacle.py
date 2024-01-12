import turtle
from turtle import Turtle
import random

obstacle_y_positions = [-220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120,
                        140, 160, 180, 200]
obstacle_x_positions = [220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390,
                        400, 410, 420, 430, 440, 450, 460, 470, 480, 490]


color_list = [(233, 160, 50), (21, 92, 173), (49, 124, 56), (205, 76, 100), (238, 216, 66), (216, 124, 163), (10, 21, 81), (155, 8, 50), (237, 163, 179), (102, 197, 180), (226, 169, 13), (67, 34, 9), (22, 56, 141), (248, 222, 2), (153, 167, 192), (106, 5, 77), (165, 65, 85), (7, 111, 47), (21, 177, 19), (86, 75, 195), (211, 98, 26), (243, 174, 171), (179, 185, 211), (155, 214, 182), (213, 82, 59), (12, 72, 36)]
turtle.colormode(255)


class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_obs = []
        self.moving_speed = 5
        self.bound_limit = 6

    def create_obs(self):
        random_chance = random.randint(0, self.bound_limit)
        if random_chance == 1:
            new_obs = Turtle("square")
            new_obs.shapesize(stretch_wid=1, stretch_len=2)
            new_obs.penup()
            new_obs.color(random.choice(color_list))
            new_obs.setheading(180)
            random_y = random.randint(-250, 250)
            new_obs.goto(300, random_y)
            self.all_obs.append(new_obs)

    def move_obs(self):
        for obs in self.all_obs:
            obs.forward(self.moving_speed)

    def increase_moving_speed(self):
        self.bound_limit -= 1
