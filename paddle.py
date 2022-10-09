from turtle import Turtle

class Field:
    def __init__(self):
        self.paddle1 = []
        self.paddle2= []
        self.create_paddle1()
        self.create_paddle2()
        self.create_halfcourt()

    def up1(self):
        if self.paddle1[0].ycor() < 370:

            for _ in range(len(self.paddle1) -1, 0,-1):
                xcor = self.paddle1[_-1].xcor()
                ycor = self.paddle1[_-1].ycor()+20
                self.paddle1[_].setposition(x=xcor,y=ycor)

            self.paddle1[0].setheading(90)
            self.paddle1[0].forward(20)
            self.paddle1[0].forward(20)






    def down1(self):
        if self.paddle1[2].ycor() > -368:
            for _ in range(len(self.paddle1) -1):
                xcor = self.paddle1[_+1].xcor()
                ycor = self.paddle1[_+1].ycor()-20
                self.paddle1[_].setposition(x=xcor,y=ycor)
            self.paddle1[len(self.paddle1) -1].setheading(-90)
            self.paddle1[len(self.paddle1) -1].forward(20)
            self.paddle1[len(self.paddle1) - 1].forward(20)


    def up2(self):
        if self.paddle2[0].ycor() < 370:

            for _ in range(len(self.paddle2) -1, 0,-1):
                xcor = self.paddle2[_-1].xcor()
                ycor = self.paddle2[_-1].ycor()+20
                self.paddle2[_].setposition(x=xcor,y=ycor)

            self.paddle2[0].setheading(90)
            self.paddle2[0].forward(20)
            self.paddle2[0].forward(20)


    def down2(self):
        if self.paddle2[2].ycor() > -368:
            for _ in range(len(self.paddle2) -1):
                xcor = self.paddle2[_+1].xcor()
                ycor = self.paddle2[_+1].ycor()-20
                self.paddle2[_].setposition(x=xcor,y=ycor)

            self.paddle2[len(self.paddle2) -1].setheading(-90)
            self.paddle2[len(self.paddle2) -1].forward(20)
            self.paddle2[len(self.paddle2) - 1].forward(20)




    def reset(self):
        for paddle_object in range(3):

            self.paddle1[paddle_object].setposition(x=-370, y=40 - (20 * paddle_object))

        for paddle_object in range(3):

            self.paddle2[paddle_object].setposition(x=370, y=40 - (20 * paddle_object))




    def create_paddle1(self):
        for _ in range(3):
            paddle_objects = Turtle(shape="square")
            paddle_objects.shapesize(1.4)
            paddle_objects.penup()
            paddle_objects.color("white")
            paddle_objects.setposition(x=-370, y=40 - (20 * _) )
            self.paddle1.append(paddle_objects)

    def create_paddle2(self):
        for _ in range(3):
            paddle_objects = Turtle(shape="square")
            paddle_objects.shapesize(1.4)
            paddle_objects.penup()
            paddle_objects.color("white")
            paddle_objects.setposition(x=370, y=30 - (20 * _))
            self.paddle2.append(paddle_objects)

    def create_halfcourt(self):
        for _ in range(20):
            paddle_objects = Turtle(shape="square")
            paddle_objects.shapesize(.75,.25)
            paddle_objects.penup()
            paddle_objects.color("white")
            paddle_objects.setposition(x=0, y=-380 + (40* _))



