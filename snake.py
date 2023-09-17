from turtle import Turtle, Screen
import random
from snake_game import SnakeGame
screen = Screen()
SNAKE_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class SnakeMove:
    def __init__(self, food):
        self.snake_objects_list = []
        self.create_snake_objects()
        self.head = self.snake_objects_list[0]
        self.food = food



    def create_snake_objects(self):
        # creating 3 snakes(Objects)
        # x = 0
        # y = 0
        # for i in range(3):
        #     snake = Turtle("square")
        #     snake.color("white")
        #     snake.shapesize(2,2)
        #     snake.goto(x, y)
        #     x -= 20
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


    # def move_new(self):
        # snake_objects_list[2].goto(0, snake_objects_list[0].ycor() + 20)
        # snake_objects_list[2].left(90)
        # snake_objects_list[2].forward(20)
        # snake_objects_list[0].left(90)
        # snake_objects_list[0].forward(20)
        # snake_objects_list[1].forward(20)
        # snake_objects_list[1].left(90)
        # this is just an idea that only move the tail square to the aimed position. like for left turn, i can just move the third one
        # above the first one. to achieve this, it needs to change the index of the objects  in the list each time, it require some
        # sort of data structure skill which i haven't touched yet.

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
        food.clear()
        new_snake_object = Turtle("square")
        new_snake_object.color("white")
        new_snake_object.goto(food)
        self.snake_objects_list.insert(0,new_snake_object)
        self.snake_objects_list[0] = new_snake_object


    def next_step(self):
        head_x = self.head.xcor()
        head_y = self.head.ycor()
        return head_x, head_y