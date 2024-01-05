from turtle import Turtle # Import the Turtle class
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # Snake starting positions
MOVE_DISTANCE = 15 # Distance to move the snake
DIRECTION_UP = 90 # Degrees to move up
DIRECTION_DOWN = 270 # Degrees to move down
DIRECTION_LEFT = 180 # Degrees to move left
DIRECTION_RIGHT = 0 # Degrees to move right

class Snake:
    """ Creates a new snake object """
    
    def __init__(self, screen):
        self.segments = [ ] # List of segments
        self.create_snake( )
        self.head = self.segments[ 0 ] # Get the head of the snake
        self.screen = screen

    def create_snake(self):
        """ Create a snake with 3 segments """

        for position in STARTING_POSITIONS:
            new_segment = Turtle( "square" ) # Create a new segment
            new_segment.towards
            new_segment.color( "white" ) # Set the color of the segment
            new_segment.penup( ) # Don't draw a line when moving
            new_segment.goto( position ) # Move the segment to the position
            self.segments.append( new_segment ) # Add the segment to the list of segments

    def move(self):
        """ Move the snake forward 20 pixels """

        for seg_num in range( len( self.segments ) - 1, 0, -1 ):
            new_pos = self.segments[ seg_num - 1 ].position( ) # Get the position of the previous segment
            self.segments[ seg_num ].goto( new_pos )
    
        self.head.forward( MOVE_DISTANCE ) # Move the first segment forward

    def up(self):
        """ Move the snake up """

        if( self.head.heading( ) != DIRECTION_DOWN ):
            self.head.setheading( DIRECTION_UP )
            self.refresh_screen( self.screen, True ) # Refresh the screen


    def down(self):
        """ Move the snake down """

        if( self.head.heading( ) != DIRECTION_UP ):
            self.head.setheading( DIRECTION_DOWN )
            self.refresh_screen( self.screen, True ) # Refresh the screen

    def left(self):
        """ Move the snake left """

        if( self.head.heading( ) != DIRECTION_RIGHT ):
            self.head.setheading( DIRECTION_LEFT )
            self.refresh_screen( self.screen, True ) # Refresh the screen

    def right(self):
        """ Move the snake right """

        if( self.head.heading( ) != DIRECTION_LEFT ):
            self.head.setheading( DIRECTION_RIGHT )
            self.refresh_screen( self.screen, True ) # Refresh the screen

    def refresh_screen( self, screen, should_refresh ):
        if( should_refresh ):
            screen.update( ) # Update the screen

    def eat_food(self):
        # Logic to handle when the snake eats food
        pass

    def check_collision(self):
        # Logic to check if the snake collides with itself or the boundaries
        pass
