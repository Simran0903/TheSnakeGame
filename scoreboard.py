from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial', 14, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.score=0
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def write_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1
