from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("best_score.txt") as b_s:
            self.high_score = int(b_s.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color('white')
        self.write(arg=f'Score: {self.score}, best score: {self.high_score}', move=False, align="center", font=("Courier", 20, "normal"))


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        with open("best_score.txt", mode="w") as data:
            data.write(f"{self.high_score}")

        self.write(arg=f'Score: {self.score}, best score: {self.high_score}', move=False, align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='Game over', move=False, align="center", font=("Courier", 20, "normal"))

    def goodbye(self):
        self.color('blue')
        self.goto(0, 0)
        self.write(arg='Goodbye', move=False, align="center", font=("Courier", 20, "normal"))

    def inc_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f'Score: {self.score}, best score: {self.high_score}', move=False, align="center", font=("Courier", 20, "normal"))

