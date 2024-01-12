from turtle import Turtle
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.fullSnake = []

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake_block(position)

    def add_snake_block(self, position):
        new_snake_block = Turtle("square")
        new_snake_block.penup()
        new_snake_block.color("white")
        new_snake_block.goto(position)
        self.fullSnake.append(new_snake_block)

    def extend(self):
        self.add_snake_block(self.fullSnake[-1].position())

    def move(self):
        for i in range(len(self.fullSnake) - 1, 0, -1):
            new_x_pos = self.fullSnake[i - 1].xcor()
            new_y_pos = self.fullSnake[i - 1].ycor()
            self.fullSnake[i].goto(new_x_pos, new_y_pos)
        self.fullSnake[0].forward(20)

    def turn_up(self):
        if self.fullSnake[0].heading() != DOWN:
            self.fullSnake[0].setheading(UP)

    def turn_left(self):
        if self.fullSnake[0].heading() != RIGHT:
            self.fullSnake[0].setheading(LEFT)

    def turn_down(self):
        if self.fullSnake[0].heading() != UP:
            self.fullSnake[0].setheading(DOWN)

    def turn_right(self):
        if self.fullSnake[0].heading() != LEFT:
            self.fullSnake[0].setheading(RIGHT)

    def reset(self):
        for lilSnake in self.fullSnake:
            lilSnake.goto(1000, 1000)
        self.fullSnake.clear()
        self.create_snake()

# Long way
    # def turn_up(self):
    #     i = 0
    #     self.fullSnake[0].setheading(90)
    #     while i < len(self.fullSnake):
    #         for i in range(1, len(self.fullSnake)):
    #             self.fullSnake[i].goto(self.fullSnake[i - 1].xcor(), self.fullSnake[i - 1].ycor())
    #         self.fullSnake[0].forward(20)
    #         i += 1
    #     for i in range(1, len(self.fullSnake)):
    #         self.fullSnake[i].setheading(90)
    #     self.fullSnake[len(self.fullSnake) - 1].backward(20)
    #
    # def turn_left(self):
    #     i = 0
    #     self.fullSnake[0].setheading(180)
    #     while i < len(self.fullSnake):
    #         for i in range(1, len(self.fullSnake)):
    #             self.fullSnake[i].goto(self.fullSnake[i - 1].xcor(), self.fullSnake[i - 1].ycor())
    #         self.fullSnake[0].forward(20)
    #         i += 1
    #     for i in range(1, len(self.fullSnake)):
    #         self.fullSnake[i].setheading(180)
    #     self.fullSnake[len(self.fullSnake) - 1].backward(20)
    #
    # def turn_right(self):
    #     i = 0
    #     if self.fullSnake[0].heading() = 180
    #     self.fullSnake[0].setheading(360)
    #     while i < len(self.fullSnake):
    #         for i in range(1, len(self.fullSnake)):
    #             self.fullSnake[i].goto(self.fullSnake[i - 1].xcor(), self.fullSnake[i - 1].ycor())
    #         self.fullSnake[0].forward(20)
    #         i += 1
    #     for i in range(1, len(self.fullSnake)):
    #         self.fullSnake[i].setheading(360)
    #     self.fullSnake[len(self.fullSnake) - 1].backward(20)
    #
    # def turn_down(self):
    #     i = 0
    #     self.fullSnake[0].setheading(270)
    #     while i < len(self.fullSnake):
    #         for i in range(1, len(self.fullSnake)):
    #             self.fullSnake[i].goto(self.fullSnake[i - 1].xcor(), self.fullSnake[i - 1].ycor())
    #         self.fullSnake[0].forward(20)
    #         i += 1
    #     for i in range(1, len(self.fullSnake)):
    #         self.fullSnake[i].setheading(270)
    #     self.fullSnake[len(self.fullSnake) - 1].backward(20)
