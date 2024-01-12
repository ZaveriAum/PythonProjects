import time
from turtle import Screen
from player import CrossingTurtle
from obstacle import Obstacle
from score_board import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player1 = CrossingTurtle()
obstacle = Obstacle()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=player1.move, key="Up")
screen.onkey(fun=player1.move_back, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if player1.reset_position():
        score_board.increase_level()
        obstacle.increase_moving_speed()
    screen.update()

    obstacle.create_obs()
    obstacle.move_obs()

    # detect collision
    for obs in obstacle.all_obs:
        if obs.distance(player1) < 20:
            game_is_on = False
            break
