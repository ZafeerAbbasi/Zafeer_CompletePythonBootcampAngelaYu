from turtle import Turtle

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_INITIAL_XPOSITION = 350
PADDLE_INITIAL_YPOSITION = 0

class Paddle( Turtle ):

    def __init__( self, xy_pos ):

        super().__init__( )
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=( PADDLE_HEIGHT / 20 ), stretch_len=( PADDLE_WIDTH / 20 ) )
        self.penup( )
        self.goto( xy_pos )

    def move_up( self ):
        new_y = self.ycor( ) + 20
        self.goto( self.xcor( ), new_y )

    def move_down( self ):
        new_y = self.ycor( ) - 20
        self.goto( self.xcor( ), new_y )