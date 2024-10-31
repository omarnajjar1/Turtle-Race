from turtle import Turtle, Screen
from pygame import mixer
import random
import time

mixer.init()

# Display user's screen
window = Screen()
window.setup(1100, 800)
window.title("Turtle Race")
window.bgcolor("black")

# Reserve the colors and positions for the turtles
colors = ('red','blue','green')
y_positions = (-250,0,250)
turtles = []

# This turtle for writing
writingTurtle = Turtle()
writingTurtle.hideturtle()

# Draw the gray race track
grawTurtle = Turtle()
grawTurtle.hideturtle()
grawTurtle.color("gray")
grawTurtle.speed("fastest")
grawTurtle.penup()
grawTurtle.goto(-550, -400)
grawTurtle.begin_fill()
grawTurtle.setheading(0)
grawTurtle.forward(930)
grawTurtle.left(90)
grawTurtle.forward(800)
grawTurtle.left(90)
grawTurtle.forward(930)
grawTurtle.left(90)
grawTurtle.forward(800)
grawTurtle.end_fill()

# Draw the final white line for the race
whiteTurtle = Turtle()
whiteTurtle.hideturtle()
whiteTurtle.color('white')
whiteTurtle.pensize(20)
whiteTurtle.penup()
whiteTurtle.goto(380,-400)
whiteTurtle.setheading(90)
whiteTurtle.pendown()
whiteTurtle.forward(800)

# Create the racing turtles
for i in range(3):
    new_turtle = Turtle('turtle') 
    new_turtle.shapesize(2)
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-500, y_positions[i])
    turtles.append(new_turtle)

def set_up():
    "Return the racing turtles to the starting point"
    for i in range(3):
        turtles[i].goto(-500, y_positions[i])

def check_result():
    "Check if any turtle reached the finish line"
    for turtle in turtles:
        if turtle.xcor() > 380:
            return turtle.pencolor()

def display_result(guessing: str, winner: str):
    "Display the result of the game"
    if guessing == winner:
        writingTurtle.write("You win!", align= "center", font= ("Arial", 40, "bold"))
        mixer.music.load(r"win_sound.mp3")
    else:
        writingTurtle.write("You Lose!", align= "center", font= ("Arial", 40, "bold"))
        mixer.music.load(r"lose_sound3.mp3")
    mixer.music.play()
    time.sleep(2)

# Run the game
while True:
    guessing = window.textinput("Make your bet", "Guess the winner: \nType a color: Red, Blue or Green ?").lower()
    if guessing in ["blue", "red", "green"]:
        mixer.music.load(r"starting_game_sound.mp3")  
        mixer.music.play()
        time.sleep(3)
        mixer.music.load(r"exiting_match_sound.mp3")
        mixer.music.play()
    elif guessing == 'exit':
        quit()
    else:
        writingTurtle.color("orange")
        writingTurtle.write("Invalid Choice", align= "center", font= ("Arial", 30, "bold"))
        time.sleep(2)
        writingTurtle.clear()
        continue

    while True:
        for turtle in turtles:
            turtle.forward(random.randint(1,5))
            winner = check_result()
        if winner:
            writingTurtle.color(winner)
            display_result(guessing, winner)
            writingTurtle.clear()
            set_up()
            break    
