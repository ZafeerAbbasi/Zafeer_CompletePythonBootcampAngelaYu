from turtle import Turtle
import time

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_INITIAL_XPOSITION = 350
PADDLE_INITIAL_YPOSITION = 0
BALL_X_SPEED_MULTIPLIER = 2
BALL_Y_SPEED_MULTIPLIER = 2


class Ball( Turtle ):

    def __init__( self ):
        super( ).__init__( )

        self.shape( "square" )
        self.color( "white" )  
        self.penup( )
        self.goto( 0, 0 )
        self.x_move = 1 * BALL_X_SPEED_MULTIPLIER
        self.y_move = 1 * BALL_Y_SPEED_MULTIPLIER

    def move( self ):
        new_x = self.xcor( ) + self.x_move
        new_y = self.ycor( ) + self.y_move
        self.goto( new_x, new_y )

    def bounce_y( self ):
        self.y_move *= -1

    def bounce_x( self ):
        self.x_move *= -1
