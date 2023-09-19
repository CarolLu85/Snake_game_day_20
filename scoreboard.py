from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("pink")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)

    def calculate_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, "center", ('Arial', 28, 'normal'))





    # def calculate_scores(self, points):
    #     self.write(f"Score: {points} ", False, "center")
