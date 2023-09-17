from turtle import Turtle
from snake import SnakeMove
import random
class SnakeGame:
    def __init__(self):
        self.snake = SnakeMove()
        self.create_food()


    def create_food(self):
        self.food = Turtle("square")
        self.food.color("pink")
        self.food.penup()
        self.food.goto(random.randint(-300, 300), random.randint(-300, 300))
        self.x = self.food.xcor()
        self.y = self.food.ycor()


    def game_over(self, x, y):
        game_over = False
        if abs(x) == 290 or abs(y) == 290:
            game_over = True
            print("You lose")
            return game_over

