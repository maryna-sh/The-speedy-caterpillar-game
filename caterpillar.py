from turtle import Turtle
import turtle as t
import random

COORDINATE = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
t.colormode(255)
colors = [(168, 230, 207), (220, 237, 193), (255, 211, 182), (255, 170, 165), (255, 139, 148)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in COORDINATE:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("circle")
        snake.speed("fastest")
        snake.penup()
        snake.color(random.choice(colors))
        snake.goto(position)
        self.snakes.append(snake)


    def extend(self):
        self.add_segment(self.snakes[-1].position())



    def move(self):
        for sn in range(len(self.snakes) -1, 0, -1):
            new_x = self.snakes[sn - 1].xcor()
            new_y = self.snakes[sn - 1].ycor()
            self.snakes[sn].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)


    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)