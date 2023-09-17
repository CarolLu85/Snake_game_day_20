from turtle import Turtle, Screen
# from snake import Snake
from snake_game import SnakeGame

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
# create objects
# snake = Snake()
game = SnakeGame(screen)






game.play_game()




screen.exitonclick()
