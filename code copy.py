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
turtle.penup()
turtle.goto(-270,-90)
turtle.write("The game will start in 5 seconds!",font=("Arial", 30, "normal"))
time.sleep(5)
turtle.clearscreen()  # Clear the turtle window before switching to the console game

# --- Hint System ---
# Takes the player's guess and the secret number and returns a hot/cold hint
def hint(guess, secret):
    diff = abs(guess - secret)  # How far off the guess is
    if diff == 0:
        return "Exactly right!"
    elif diff <= 5:
        return "Scorching hot!"
    elif diff <= 15:
        return "Very warm!"
    elif diff <= 30:
        return "Warm..."
    elif diff <= 60:
        return "Cold."
    else:
        return "Freezing!"

# --- Single Round Logic ---
# Handles one round of the guessing game; returns whether the player won and their score
def play_round(round_num, high, lives):
    secret = random.randint(1, high)  # Pick a random secret number
    remaining = lives
    guesses = []  # Track all guesses made this round

    print(f"\n--- Level {round_num} ---")
    print(f"Guess a number between 1 and {high}. You have {lives} lives.")

    while remaining > 0:
        try:
            raw = input(f"\n[Lives: {remaining}] Your guess: ").strip()
            guess = int(raw)  # Convert input to an integer
        except ValueError:
            print("Please enter a valid number.")
            continue  # Ask again if input wasn't a number

        # Make sure the guess is within the valid range
        if guess < 1 or guess > high:
            print(f"Out of range! Pick between 1 and {high}.")
            continue

        guesses.append(guess)
        h = hint(guess, secret)
        print(f"  {h}", end="  ")

        if guess == secret:
            # Score = lives remaining * 10 + bonus for guessing quickly
            score = remaining * 10 + max(0, (5 - len(guesses)) * 5)
            print(f"\nCorrect! The number was {secret}.")
            print(f"You got it in {len(guesses)} guess(es). +{score} points!")
            return True, score

        elif guess < secret:
            print("Go higher! ↑")
        else:
            print("Go lower! ↓")

        remaining -= 1  # Use up a life after each wrong guess

    print(f"\nOut of lives! The number was {secret}.")
    return False, 0  # Player lost this round

# --- Banner ---
# Prints a decorative title header to the console
def banner():
    print("=" * 40)
    print("        THE NUMBER GAME")
    print("=" * 40)

# --- Main Game Loop ---
# Runs the full game: intro, all rounds, score summary, and play again prompt
def game():
    banner()
    name = input("\nWhat's your name? ").strip() or "Player"  # Default to "Player" if blank
    print(f"\nWelcome, {name}!")
    time.sleep(0.5)

    high, lives, diff_name = get_difficulty()  # Unpack difficulty settings
    total_score = 0
    max_levels = 5  # Total number of rounds per game

    print(f"\nDifficulty: {diff_name} | {max_levels} rounds to play. Good luck!\n")
    time.sleep(1)

    # Loop through each round
    for round_num in range(1, max_levels + 1):
        won, points = play_round(round_num, high, lives)
        total_score += points
        if not won:
            print(f"Better luck next round! Score so far: {total_score}")

    # Show end-of-game summary
    print("\n" + "=" * 40)
    print(f"  Game Over, {name}!")
    print(f"  Final Score: {total_score} / {max_levels * (lives * 10 + 20)}")

    # Give a performance message based on the score
    if total_score >= max_levels * 60:
        print("  AMAZING performance! You're a legend!")
    elif total_score >= max_levels * 30:
        print("  Good job! Keep practicing!")
    else:
        print("  Nice try — come back for revenge!")
    print("=" * 40)

    # Ask if the player wants to play again
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        game()  # Restart the game
    else:
        print(f"\nThanks for playing, {name}! See you next time!")

# Only run the game if this file is executed directly (not imported)
if __name__ == "__main__":
    game()




#Turning things into turtle.