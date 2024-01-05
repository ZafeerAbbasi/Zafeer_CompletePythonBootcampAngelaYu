from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_INITIAL_XPOSITION = 350
PADDLE_INITIAL_YPOSITION = 0


def update_screen( screen ):
    screen.update( )

def listen_for_events( screen, r_paddle, l_paddle ):
    screen.listen( )
    screen.onkeypress( r_paddle.move_up, "Up" )
    screen.onkeypress( r_paddle.move_down, "Down" )
    screen.onkeypress( l_paddle.move_up, "w" )
    screen.onkeypress( l_paddle.move_down, "s" ) 

# Create a screen
def create_screen( ):
    screen = Screen( )
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Pong")
    screen.bgcolor("black")
    screen.tracer(0)
    return screen



def main( ):
    screen = create_screen( )
    r_paddle = Paddle( xy_pos=( PADDLE_INITIAL_XPOSITION, PADDLE_INITIAL_YPOSITION ) )
    l_paddle = Paddle( xy_pos=( -PADDLE_INITIAL_XPOSITION, PADDLE_INITIAL_YPOSITION ) )
    ball = Ball( )
    listen_for_events( screen, r_paddle, l_paddle )

    while( True ):
        ball.move( )
        update_screen( screen )
        time.sleep( 0.01 )

        #Detect collision with wall
        if( ball.ycor( ) > 280 or ball.ycor( ) < -280 ):
            ball.bounce_y( )

        #Detect collision with paddle
        if( ( ball.distance( r_paddle ) < 50 and ball.xcor( ) > 320 ) or ( ball.distance( l_paddle ) < 50 and ball.xcor( ) < -320 ) ):
            ball.bounce_x( )
          


    screen.exitonclick( )

if __name__ == "__main__": # Run the game
    main( )


