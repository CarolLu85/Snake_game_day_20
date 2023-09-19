from turtle import Screen
from snake import Snake
import time
from scoreboard import ScoreBoard
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

# create objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
points = 0

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.5)
# detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.clear()
        print("nom,nom,nom")
        x = food.xcor()
        y = food.ycor()
        points += 1
        scoreboard.calculate_scores(points)
        food.refresh()
        snake.new_head(x, y)
        time.sleep(0.5)





screen.exitonclick()
