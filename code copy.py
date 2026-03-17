#This is a non AI Sesion insteace. Pracrice makes pefecrt. 
import turtle
import random
import time

def start():
    turtle.speed(10) 
    turtle.circle(100)
    turtle.goto(0,50)
    turtle.circle(50)
    turtle.penup()
    turtle.goto(0,90)
    turtle.write("The number game", align="Center")
turtle.hideturtle()
start()

#This is where the code for the inout of the game begins.
screen = turtle.Screen()
level=screen.textinput("Eneter the level you want to play", "1 for easy, 2 for medium, 3 for hard")

def get_difficulty():
    if level == "1":
        return 50, 10, "Easy"
    elif level == "3":
        return 200, 5, "Hard"
    else:
        return 100, 7, "Medium"

turtle.penup()
turtle.goto(-40,75)
turtle.write(f"You entered: {level}")

turtle.penup()
turtle.goto(-270,-90)
turtle.write("The game will start in 5 seconds!",font=("Arial", 30, "normal"))
time.sleep(3)


turtle.clearscreen()
















turtle.mainloop()