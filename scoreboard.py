from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.goto(-280,250)
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)



    def increment_level(self):
        self.level+=1
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)

