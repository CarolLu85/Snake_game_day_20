from turtle import Turtle, Screen
import time
from snake import SnakeMove
from snake_game import SnakeGame


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
snake = SnakeMove()
game = SnakeGame()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
game.create_food()

game_on = True

while game_on:
    game.game_over()

    snake.move()

    screen.update()
    time.sleep(0.1)







screen.exitonclick()
