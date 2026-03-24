import turtle
import random
import time
import math

# --- Screen Setup ---
screen = turtle.Screen()
screen.title("The Number Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Single turtle used for all text drawing
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed(0)

def clear():
    writer.clear()

def write_at(x, y, text, color="white", font=("Arial", 16, "normal")):
    writer.color(color)
    writer.goto(x, y)
    writer.write(text, align="left", font=font)

def draw_eye():
    eye = turtle.Turtle()
    eye.hideturtle()
    eye.speed(0)
    eye.penup()
    cx, cy = 0, -120

    # Eye white 
    eye.color("#c0c0c0")
    eye.begin_fill()
    for i in range(101):
        angle = 2 * math.pi * i / 100
        x = cx + 165 * math.cos(angle)
        y = cy + 90 * math.sin(angle)
        eye.goto(x, y) if i else (eye.penup(), eye.goto(x, y), eye.pendown())
    eye.end_fill()

    # eye pt 1
    eye.penup()
    eye.goto(cx, cy - 78)
    eye.color("black")
    eye.begin_fill()
    eye.circle(78)
    eye.end_fill()

    # eye
    for (hx, hy, hr) in [(-28, cy + 18, 9), (18, cy + 24, 5)]:
        eye.penup()
        eye.goto(hx, hy)
        eye.color("white")
        eye.begin_fill()
        eye.circle(hr)
        eye.end_fill()

    return eye

# --- Intro Animation ---
def start():
    intro = turtle.Turtle()
    intro.speed(10)
    intro.color("Red")
    intro.penup()
    intro.goto(0, -50)
    intro.pendown()
    intro.circle(100)
    intro.penup()
    intro.goto(0, 0)
    intro.pendown()
    intro.circle(50)
    intro.penup()
    intro.goto(0, 25)
    intro.color("yellow")
    intro.write("The Number Game", align="center", font=("Arial", 24, "bold"))
    intro.hideturtle()
    time.sleep(2)
    intro.clear()

# --- Hint System ---
def hint(guess, secret):
    diff = abs(guess - secret)
    if diff == 0:
        return "Exactly right!", "Green"
    elif diff <= 5:
        return "STILL NOT CLOSE DUMMY!", "red"
    elif diff <= 15:
        return "I guess thats close...", "orange"
    elif diff <= 30:
        return "Eh...", "yellow"
    elif diff <= 60:
        return "NAH.", "White"
    else:
        return "Freezing!", "lightblue"

# --- Single Round ---
def play_round(round_num, high, lives, name, total_score):
    secret = random.randint(1, high)
    remaining = lives
    guesses = []

    while remaining > 0:
        clear()
        write_at(-390, 260, f"Round {round_num}  |  Player: {name}  |  Score: {total_score}",
                 color="yellow", font=("Arial", 14, "normal"))
        write_at(-390, 225, f"Guess a number between 1 and {high}",
                 color="white", font=("Arial", 16, "normal"))
        write_at(-390, 190, f"Lives: {'♥ ' * remaining}",
                 color="red", font=("Arial", 16, "normal"))
        if guesses:
            write_at(-390, 155, f"Previous guesses: {', '.join(map(str, guesses))}",
                     color="gray", font=("Arial", 13, "normal"))

        raw = screen.numinput(
            f"Round {round_num} — Lives: {remaining}",
            f"Guess a number between 1 and {high}:",
            minval=1, maxval=high
        )

        if raw is None:
            # Player closed the dialog — count as a skip
            remaining -= 1
            continue

        guess = int(raw)
        guesses.append(guess)
        h, color = hint(guess, secret)

        clear()
        write_at(-390, 260, f"Round {round_num}  |  Player: {name}  |  Score: {total_score}",
                 color="yellow", font=("Arial", 14, "normal"))
        write_at(-390, 225, f"Guess a number between 1 and {high}",
                 color="white", font=("Arial", 16, "normal"))
        write_at(-390, 190, f"Lives: {'*' * remaining}",
                 color="red", font=("Arial", 16, "normal"))
        write_at(-390, 155, f"Previous guesses: {', '.join(map(str, guesses))}",
                 color="gray", font=("Arial", 13, "normal"))
        write_at(-390, 110, f"Hint: {h}", color=color, font=("Arial", 22, "bold"))

        if guess == secret:
            score = remaining * 10 + max(0, (5 - len(guesses)) * 5)
            write_at(-390, 60,  f"Correct! The number was {secret}!", color="lime",   font=("Arial", 18, "bold"))
            write_at(-390, 25,  f"Guessed in {len(guesses)} try/tries. +{score} points!", color="white", font=("Arial", 15, "normal"))
            time.sleep(2)
            return True, score
        elif guess < secret:
            write_at(-390, 60, "Go higher!  ↑", color="orange", font=("Arial", 17, "normal"))
        else:
            write_at(-390, 60, "Go lower!  ↓", color="orange", font=("Arial", 17, "normal"))

        remaining -= 1
        time.sleep(1.2)

    clear()
    write_at(-390, 100, f"Out of lives!  The number was {secret}.",
             color="red", font=("Arial", 18, "bold"))
    time.sleep(2)
    return False, 0

# --- Main Game ---
def game():
    start()

    name = screen.textinput("Welcome!", "What's your name?") or "Player"

    # If the user typed a number instead of a name — trigger the creepy sequence
    try:
        float(name.strip())
        is_num = True
    except (ValueError, TypeError):
        is_num = False

    if is_num:
        clear()
        write_at(-340, 180, "This isn't that type of game.", color="white", font=("Arial", 22, "bold"))
        write_at(-110, 130, "I see you", color="red", font=("Arial", 28, "bold"))
        eye_turtle = draw_eye()
        time.sleep(10)
        eye_turtle.clear()
        clear()
        screen.bye()
        return

    level = screen.textinput("Choose Difficulty",
                             "Enter level:\n  1 = Easy (1–50, 10 lives)\n  2 = Medium (1–100, 7 lives)\n  3 = Hard (1–200, 5 lives)")

    if level == "1":
        high, lives, diff_name = 50, 10, "Easy"
    elif level == "3":
        high, lives, diff_name = 200, 5, "Hard"
    else:
        high, lives, diff_name = 100, 7, "Medium"

    max_levels = 5
    total_score = 0

    clear()
    write_at(-390, 260, f"Welcome, {name}!", color="cyan", font=("Arial", 24, "bold"))
    write_at(-390, 215, f"Difficulty: {diff_name}  |  {max_levels} rounds  |  Numbers 1–{high}", color="white", font=("Arial", 16, "normal"))
    write_at(-390, 175, "Good luck!", color="yellow", font=("Arial", 18, "normal"))
    time.sleep(2.5)

    for round_num in range(1, max_levels + 1):
        won, points = play_round(round_num, high, lives, name, total_score)
        total_score += points
        if not won:
            clear()
            write_at(-390, 100, f"Bad luck this round!  Score so far: {total_score}",
                     color="orange", font=("Arial", 16, "normal"))
            time.sleep(2)

    # End-of-game summary
    max_possible = max_levels * (lives * 10 + 20)
    clear()
    write_at(-390, 260, "=" * 44, color="yellow", font=("Arial", 14, "normal"))
    write_at(-300, 220, f"Game Over, {name}!", color="cyan", font=("Arial", 24, "bold"))
    write_at(-390, 175, f"Final Score: {total_score} / {max_possible}", color="white", font=("Arial", 18, "bold"))

    if total_score >= max_levels * 60:
        msg, col = "AMAZING performance!  You're a legend!", "gold"
    elif total_score >= max_levels * 30:
        msg, col = "Good job!  Keep practicing!", "lime"
    else:
        msg, col = "Nice try — come back for revenge!", "orange"

    write_at(-390, 130, msg, color=col, font=("Arial", 16, "bold"))
    write_at(-390, 85,  "=" * 44, color="yellow", font=("Arial", 14, "normal"))

    again = screen.textinput("Play Again?", "Play again? (y / n):")
    if again and again.strip().lower() == "y":
        clear()
        game()
    else:
        clear()
        write_at(-350, 0, f"Thanks for playing, {name}!  See you next time!",
                 color="cyan", font=("Arial", 18, "normal"))
        time.sleep(3)
        screen.bye()

if __name__ == "__main__":
    game()
    turtle.mainloop()
