import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

python = Snake()
food = Food()
screen = Screen()
scoreBoard = ScoreBoard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Genji's snake game.")
screen.tracer(0)

python.create_snake()

game_is_on = True

screen.listen()
screen.onkey(fun=python.turn_up, key="Up")
screen.onkey(fun=python.turn_left, key="Left")
screen.onkey(fun=python.turn_right, key="Right")
screen.onkey(fun=python.turn_down, key="Down")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    python.move()

    # Detect the distance
    if python.fullSnake[0].distance(food) < 15:
        food.refresh()
        python.extend()
        scoreBoard.increase_score()

    if python.fullSnake[0].xcor() > 290 or python.fullSnake[0].xcor() < -290 or python.fullSnake[0].ycor() > 290 or \
            python.fullSnake[0].ycor() < -290:
        scoreBoard.reset()
        python.reset()

    for lilSnake in python.fullSnake[1:]:
        if python.fullSnake[0].distance(lilSnake) < 10:
            scoreBoard.reset()
            python.reset()
screen.exitonclick()
