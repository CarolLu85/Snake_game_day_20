from turtle import Screen
from update_snake import Snake
import time
from updated_scoreboard import ScoreBoard
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


while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.4)
# detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.clear()
        food.refresh()
        snake.new()
        scoreboard.calculate_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for each_square in snake.snake_objects_list[1:]:
        # if each_square == snake.head:
        #     pass
        if snake.head.distance(each_square) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
