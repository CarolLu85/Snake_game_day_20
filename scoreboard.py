from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("pink")
        self.goto(0, 270)
        self.write(f"Score: {self.score} ", False, "center", ('Arial', 20, 'normal'))






    # def calculate_scores(self, points):
    #     self.write(f"Score: {points} ", False, "center")
