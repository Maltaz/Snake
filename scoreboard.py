from turtle import Turtle

#CONSTANS
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.speed("fastest")
        self.write(f"Score {self.score}", align=ALIGMENT, font=(FONT, 24, "normal"))

    def update_scoreboard(self):
        """Docstring"""
        self.clear()
        self.write(f"Score {self.score} High score {self.high_score}", align=ALIGMENT, font=(FONT, 24, "normal"))

    def reset(self):
        """Docstring"""

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase(self):
        """Docstring"""

        self.score += 1
        self.clear()
        self.update_scoreboard()



