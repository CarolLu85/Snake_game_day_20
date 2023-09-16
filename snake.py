from turtle import Turtle, Screen
screen = Screen()
class SnakeMove:
    def __init__(self, ):
        self.shape = "square"
        self.penup()
        screen.bgcolor("black")


        for index in snake_coordinates:
            snake_object = Turtle("square")
            snake_object.color("white")
            snake_object.penup()
            snake_object.goto(index)
            position = snake_object.position()
            print(position)
            snake_objects_list.append(snake_object)
    def move(self):
        for object_index in range(len(snake_objects_list) - 1, 0, -1):
            # get the coordinates of the object_index-1 object.
            x = snake_objects_list[object_index - 1].xcor()
            y = snake_objects_list[object_index - 1].ycor()
            snake_objects_list[object_index].goto(x, y)

        snake_objects_list[0].forward(20)

    def