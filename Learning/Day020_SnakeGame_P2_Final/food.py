from turtle import Turtle
import random

class Food( Turtle ):
    """"Creates a new food object"""

    def __init__( self ):
        super( ).__init__( shape="circle" ) # Call the parent constructor
        self.penup
        self.shapesize( stretch_len=0.5, stretch_wid=0.5 )
        self.color( "blue" )
        self.teleport( x=random.randint( a=-280, b=280 ), y=random.randint( a=-280, b=260 ) )

    def refresh_food( self ):
        self.teleport( x=random.randint( a=-280, b=280 ), y=random.randint( a=-280, b=260 ) )