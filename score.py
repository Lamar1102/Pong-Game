from turtle import Turtle

class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1= 0
        self.player1score()



    def player1score(self):
         self.color("white")
         self.penup()
         self.goto(x=-250,y=380)
         self.hideturtle()
         self.clear()
         self.write(f"Score: {self.player_1}", move=False, align="center", font=("courier", 16, "normal"))

class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.player_2 = 0
        self.player2score()

    def player2score(self):
         self.color("white")
         self.penup()
         self.goto(x=150,y=380)
         self.hideturtle()
         self.clear()
         self.write(f"Score: {self.player_2}", move=False, align="center", font = ("courier", 16, "normal"))










