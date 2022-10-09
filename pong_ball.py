from turtle import Turtle
import random


class PongBall(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("slowest")
        self.penup()
        self.random_start_list = [self.start1, self.start2, self.start3, self.start4, self.start5,
                                  self.start6]
        self.random_turn_list = [self.turn1,self.turn2,self.turn3,self.turn4,self.turn5,self.turn6]

    def start(self):
        random.choice(self.random_start_list)()

    def turn(self):
        random.choice(self.random_turn_list)()

    def ball_restart(self):
        self.goto(x=0,y=0)
        random.choice(self.random_start_list)()


    def bounce_off_wall(self):


        if self.heading() > 0 and self.heading() < 90:
            angle = random.randint(280,355)
            self.setheading(angle)


        elif self.heading() > 90 and self.heading() < 180:
            angle = random.randint(190,265)
            self.setheading(angle)


        elif self.heading() > 180 and self.heading() < 270:
            self.setheading(random.randint(95,175))

        elif self.heading() > 270 and self.heading() < 360:
            self.setheading(random.randint(10,85))



    def move(self):
        self.forward(10)

    def start1(self):
        self.forward(20)

    def start2(self):
        self.setheading(180)
        self.forward(20)

    def start3(self):
        self.setheading(28)
        self.forward(20)

    def start4(self):
        self.setheading(165)
        self.forward(20)

    def start5(self):
        self.setheading(320)
        self.forward(20)

    def start6(self):
        self.setheading(215)
        self.forward(20)

    def turn1(self):
        self.setheading(self.heading()+180)

    def turn2(self):
        self.setheading(self.heading()+190)

    def turn3(self):
        self.setheading(self.heading()+210)

    def turn4(self):
        self.setheading(self.heading()+155)

    def turn5(self):
        self.setheading(self.heading()+230)

    def turn6(self):
        self.setheading(self.heading()+150)


