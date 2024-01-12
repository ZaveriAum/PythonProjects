import turtle
from turtle import Screen
from player import Player
from ball import Pong
from scoreBoard import ScoreBoard

# creating objects from classes
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Genji's Pong")

# creating a stop of loading the screen
screen.tracer(0)

scoreBoard = ScoreBoard()

player1 = Player(370, 0)
player2 = Player(-370, 0)
pong = Pong()

##############################################################################################################

# function for both paddle to go up or down
screen.listen()
screen.onkeypress(fun=player1.go_up, key="Up")
screen.onkeypress(fun=player1.go_down, key="Down")
screen.onkeypress(fun=player2.go_up, key="w")
screen.onkeypress(fun=player2.go_down, key="s")
################################################################################################################

game_is_on = True
while game_is_on:
    screen.update()
    pong.pong_move()

    if pong.xcor() > 380:
        pong.reset_position_player1()
        scoreBoard.p2_score()
        pong.reset_speed()
    elif pong.xcor() < -380:
        pong.reset_position_player2()
        scoreBoard.p1_score()
        pong.reset_speed()

    # detect collision with right player
    if pong.xcor() > 370 or pong.xcor() < -370:
        if pong.distance(player1) < 60 or pong.distance(player2) < 60:
            pong.setheading(180 - pong.heading())
            pong.increase_speed()

screen.exitonclick()
