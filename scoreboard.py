from turtle import Turtle

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()

    #refresh the scoreboard to show the new user score
    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} Highscore: {self.high_score}", align="center", font=("Ariel", 24, "normal"))

    #write and save the new highscore in the text file so that it can be reused
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    #increase the score and clear previous score everytime food is eaten
    def score_increase(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()


