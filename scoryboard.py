from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high.txt") as book:
            content = book.read()
        self.highscore =int(content)

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score = {self.score} High Score = {self.highscore} ", False, "center", ("Arial", 20, "normal"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore} ", False, "center", ("Arial", 20, "normal"))

    def reset(self):
        if int(self.score) > int(self.highscore):
            with open("high.txt", mode="w") as file:
                file.write(f"{self.score}")

        with open("high.txt") as bok:
            context = bok.read()
            self.highscore = context

        self.score = 0
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore} ", False, "center", ("Arial", 20, "normal"))