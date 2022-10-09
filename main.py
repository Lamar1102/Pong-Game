from turtle import Screen
import time
from paddle import Field
from score import Score1,Score2
from pong_ball import PongBall

 #SetupOurScreen

screen = Screen() #setting the varibale to use the Screen Class
screen.setup(width=800, height=800)
screen.bgcolor("gray")
screen.title("Pong")
#Turn off Tracer so animations of objects moving with eachother arent blotchy
screen.tracer(0)

#Classes

paddles = Field()
score1 = Score1()
score2= Score2()

pong_ball = PongBall()

screen.listen()
screen.onkeypress(paddles.up1, "w")
screen.onkeypress(paddles.down1, "s")

screen.onkeypress(paddles.up2, "Up")
screen.onkeypress(paddles.down2, "Down")



def pong_game():

    game_on = True

    while game_on:
        screen.update()
        pong_ball.start()
        while game_on:
            screen.update()
            time.sleep(.09)
            pong_ball.move()
            pong_ball.move()
            pong_ball.move()

           
            if pong_ball.distance(paddles.paddle1[1]) < 34 and pong_ball.xcor() > -368: #Detect Collision With Paddle
                pong_ball.turn()
                pong_ball.move()


            if pong_ball.distance(paddles.paddle2[1]) < 34 and pong_ball.xcor() < 368: #Detect Collision With Paddle
                pong_ball.turn()
                pong_ball.move()

            if pong_ball.ycor()>375 or pong_ball.ycor()<-375:

                pong_ball.bounce_off_wall()
                pong_ball.move()

            if pong_ball.xcor()< -430 :
                score2.player_2 +=1
                score1.player1score()
                score2.player2score()
                paddles.reset()
                pong_ball.ball_restart()
                time.sleep(.5)

            if pong_ball.xcor()> 430:
                score1.player_1 += 1
                score1.player1score()
                score2.player2score()
                paddles.reset()
                pong_ball.ball_restart()
                time.sleep(.5)

    screen.exitonclick()

pong_game()

