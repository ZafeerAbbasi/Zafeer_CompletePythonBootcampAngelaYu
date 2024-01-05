from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
    screen.onkey( snake.restart, "r" ) # Restart the game when r is pressed

def main( ):
    screen = create_turtle_screen( ) # Create a screen object
    snake = Snake( screen=screen ) # Create a new snake object
    scoreboard = Scoreboard( ) # Create a new scoreboard object
    food = Food( ) # Create a new food object
    listen_for_key_presses( screen, snake ) # Listen for key presses

    snake.game_is_on = True # Game loop
    while True:
        if snake.game_is_on:

            if( snake.is_restarted ):
                screen = create_turtle_screen( ) # Create a screen object
                snake = Snake( screen=screen ) # Create a new snake object
                scoreboard = Scoreboard( ) # Create a new scoreboard object
                food = Food( ) # Create a new food object
                listen_for_key_presses( screen, snake ) # Listen for key presses
                snake.is_restarted = False
                snake.game_is_on = True

            refresh_screen( screen, True ) # Refresh the screen
            snake.move( ) # Move the snake

            if( snake.head.distance( food ) < 15 ):
                scoreboard.increase_score( ) # Update the scoreboard
                food.refresh_food( ) # Refresh the food
                snake.extend( )
            
            # Detect collision with wall
            if snake.head.xcor( ) > 280 or snake.head.xcor( ) < -280 or snake.head.ycor( ) > 280 or snake.head.ycor( ) < -280:
                scoreboard.game_over( ) # Display game over message
                refresh_screen( screen, True ) # Refresh the screen
                snake.game_is_on = False

            # Detect collision with tail
            for segment in snake.segments[ 1: ]:
                if snake.head.distance( segment ) < 10:
                    scoreboard.game_over( )
                    refresh_screen( screen, True )
                    snake.game_is_on = False
    
        else:
            refresh_screen( screen, True )



if __name__ == "__main__": # Run the game
    main( )


