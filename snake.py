from turtle import Turtle, Screen
import random

screen = Screen()
SNAKE_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_objects_list = []
        self.create_snake_objects()
        self.head = self.snake_objects_list[0]
        self.head.speed(1)



    def create_snake_objects(self):

        for index in SNAKE_COORDINATES:
            snake_object = Turtle("square")
            snake_object.color("white")
            snake_object.penup()
            snake_object.goto(index)
            self.snake_objects_list.append(snake_object)


    def move(self):
        for object_index in range(len(self.snake_objects_list) - 1, 0, -1):
            # get the coordinates of the object_index-1 object.
            x = self.snake_objects_list[object_index - 1].xcor()
            y = self.snake_objects_list[object_index - 1].ycor()
            self.snake_objects_list[object_index].goto(x, y)

        self.head.forward(MOVE_DISTANCE)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def eat_food(self, food):
        food.hideturtle()
        new_snake_object = Turtle("square")
        new_snake_object.color("white")
        new_snake_object.goto(food.xcor(), food.ycor())
        self.snake_objects_list.insert(0, new_snake_object)


    def next_step(self):
        head_x = self.head.xcor()
        head_y = self.head.ycor()
        return head_x, head_y
