import random
import time

def banner():
    print("=" * 40)
    print("      GUESS THE NUMBER - CHALLENGE!")
    print("=" * 40)

def get_difficulty():
    print("\nChoose difficulty:")
    print("  1. Easy   (1-50,  10 lives)")
    print("  2. Medium (1-100,  7 lives)")
    print("  3. Hard   (1-200,  5 lives)")
    choice = input("\nEnter 1, 2, or 3: ").strip()
    if choice == "1":
        return 50, 10, "Easy"
    elif choice == "3":
        return 200, 5, "Hard"
    else:
        return 100, 7, "Medium"

def hint(guess, secret):
    diff = abs(guess - secret)
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

def play_round(level, high, lives):
    secret = random.randint(1, high)
    remaining = lives
    guesses = []

    print(f"\n--- Level {level} ---")
    print(f"Guess a number between 1 and {high}. You have {lives} lives.")

    while remaining > 0:
        try:
            raw = input(f"\n[Lives: {remaining}] Your guess: ").strip()
            guess = int(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > high:
            print(f"Out of range! Pick between 1 and {high}.")
            continue

        guesses.append(guess)
        h = hint(guess, secret)
        print(f"  {h}", end="  ")

        if guess == secret:
            score = remaining * 10 + max(0, (5 - len(guesses)) * 5)
            print(f"\nCorrect! The number was {secret}.")
            print(f"You got it in {len(guesses)} guess(es). +{score} points!")
            return True, score

        elif guess < secret:
            print("Go higher! ↑")
        else:
            print("Go lower! ↓")

        remaining -= 1

    print(f"\nOut of lives! The number was {secret}.")
    return False, 0

def game():
    banner()
    name = input("\nWhat's your name? ").strip() or "Player"
    print(f"\nWelcome, {name}!")
    time.sleep(0.5)

    high, lives, diff_name = get_difficulty()
    total_score = 0
    level = 1
    max_levels = 5

    print(f"\nDifficulty: {diff_name} | {max_levels} rounds to play. Good luck!\n")
    time.sleep(1)

    for level in range(1, max_levels + 1):
        won, points = play_round(level, high, lives)
        total_score += points
        if not won:
            print(f"Better luck next round! Score so far: {total_score}")

    print("\n" + "=" * 40)
    print(f"  Game Over, {name}!")
    print(f"  Final Score: {total_score} / {max_levels * (lives * 10 + 25)}")
    if total_score >= max_levels * 60:
        print("  AMAZING performance! You're a legend!")
    elif total_score >= max_levels * 30:
        print("  Good job! Keep practicing!")
    else:
        print("  Nice try — come back for revenge!")
    print("=" * 40)

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        game()
    else:
        print(f"\nThanks for playing, {name}! See you next time!")

if __name__ == "__main__":
    game()
