from turtle import Screen
from snake import Snake
from food import Food
import time


def refresh_screen( screen, should_refresh ):
    if( should_refresh ):
        screen.update( ) # Update the screen
        time.sleep( 0.08 ) # Pause the screen for 0.1 seconds

def create_turtle_screen( ):
    screen = Screen( ) # Create a screen object
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title( "My Snake Game" )
    screen.tracer( 0 ) # Turn off the animation
     
    return screen

def listen_for_key_presses( screen, snake ):
    screen.listen( ) # Listen for key presses
    screen.onkey( snake.up, "Up" ) # Move up when up arrow is pressed 
    screen.onkey( snake.down, "Down" ) # Move down when down arrow is pressed
    screen.onkey( snake.left, "Left" ) # Move left when left arrow is pressed
    screen.onkey( snake.right, "Right" ) # Move right when right arrow is pressed

def main( ):
    screen = create_turtle_screen( ) # Create a screen object
    snake = Snake( screen=screen ) # Create a new snake object
    food = Food( ) # Create a new food object
    listen_for_key_presses( screen, snake ) # Listen for key presses

    game_is_on = True # Game loop
    while game_is_on:

        refresh_screen( screen, True ) # Refresh the screen
        snake.move( ) # Move the snake

        if( snake.head.distance( food ) < 15 ):
            print( "Nom nom nom" )




if __name__ == "__main__": # Run the game
    main( )


# screen.exitonclick( ) # Exit the screen when clicked