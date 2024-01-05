from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard( Turtle ):

    def __init__( self ):
        super( ).__init__( )
        self.color( "white" )
        self.penup( )
        self.goto( 0, 260 )
        self.hideturtle( )
        self.score = 0
        self.write( f"Score: {self.score}", align=ALIGNMENT, font=FONT )

    def increase_score( self ):
        self.score += 1
        self.clear( )
        self.write( f"Score: {self.score}", align=ALIGNMENT, font=FONT )

    def game_over( self ):
        self.clear( )
        self.write( f"Final Score: { self.score }", align=ALIGNMENT, font=FONT )
        self.goto( 0, 0 )
        self.write( "GAME OVER", align=ALIGNMENT, font=FONT )
        self.goto( 0, -30 )
        self.write( "Press 'r' to restart", align=ALIGNMENT, font=FONT )
