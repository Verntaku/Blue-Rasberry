#This is a non AI Session instance. Practice makes perfect.
import turtle
import random
import time

# --- Intro Animation ---
# Draws two circles and a title on the turtle screen as an intro
def start():
    turtle.speed(10)
    turtle.circle(100)       # Draw outer circle
    turtle.goto(0,50)
    turtle.circle(50)        # Draw inner circle
    turtle.penup()
    turtle.goto(0,90)
    turtle.write("The number game", align="center")  # Write the title
    turtle.hideturtle()      # Hide the arrow cursor when done

start()

# This is where the code for the input of the game begins.
screen = turtle.Screen()
# Ask the player to choose a difficulty level via a popup box
level=screen.textinput("Enter the level you want to play", "1 for easy, 2 for medium, 3 for hard")

# Returns the max number, number of lives, and difficulty name based on the player's choice
def get_difficulty():
    if level == "1":
        return 50, 10, "Easy"    # Small range, more lives
    elif level == "3":
        return 200, 5, "Hard"   # Large range, fewer lives
    else:
        return 100, 7, "Medium" # Default to medium if anything else is entered

# Show the player what level they entered on the turtle screen
turtle.penup()
turtle.goto(-40,75)
turtle.write(f"You entered: {level}")

# Display a countdown message before the game starts
