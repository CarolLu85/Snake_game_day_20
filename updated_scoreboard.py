from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("pink")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", False, ALIGNMENT, FONT)


    def calculate_score(self):
        self.score += 1
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)


    def reset(self):
        if self.score > self. high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
