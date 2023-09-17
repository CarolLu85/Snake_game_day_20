from turtle import Turtle, Screen
import random
import time
from snake import Snake
class SnakeGame:
    def __init__(self, screen):
        self.snake = Snake()
        self.create_food()
        self.screen = screen
        screen.onkey(self.snake.up, "Up")
        screen.onkey(self.snake.down, "Down")
        screen.onkey(self.snake.left, "Left")
        screen.onkey(self.snake.right, "Right")


    def create_food(self):
        self.food = Turtle("square")
        self.food.color("pink")
        self.food.penup()
        self.food.goto(random.randint(-300, 300), random.randint(-300, 300))
        self.x = self.food.xcor()
        self.y = self.food.ycor()


    def play_game(self):
        game_on = True
        while game_on:
            x, y = self.snake.next_step()
            if abs(x - self.x) < 20 and abs(y - self.y) < 20:
                self.snake.eat_food(self.food)
                self.create_food()
            self.snake.move()
            self.screen.update()
            time.sleep(0.1)


    def game_over(self, x, y):
        game_over = False
        if abs(x) == 290 or abs(y) == 290:
            game_over = True
            print("You lose")
            return game_over



