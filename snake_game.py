from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_coordinates = [(0, 0), (-20, 0), (-40, 0)]
#creating 3 snakes(Objects)
# x = 0
# y = 0
# for i in range(3):
#     snake = Turtle("square")
#     snake.color("white")
#     snake.shapesize(2,2)
#     snake.goto(x, y)
#     x -= 20
snake_objects_list = []
for index in snake_coordinates:
    snake_object = Turtle("square")
    snake_object.color("white")
    snake_object.penup()
    snake_object.goto(index)
    position = snake_object.position()
    print(position)
    snake_objects_list.append(snake_object)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)



# snake_objects_list[2].goto(0, snake_objects_list[0].ycor() + 20)
# snake_objects_list[2].left(90)
# snake_objects_list[2].forward(20)
# snake_objects_list[0].left(90)
# snake_objects_list[0].forward(20)
# snake_objects_list[1].forward(20)
# snake_objects_list[1].left(90)





screen.exitonclick()
