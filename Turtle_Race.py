from turtle import Turtle, Screen
from pygame import mixer
import random
import time

mixer.init()

def game():
    # Display user's screen
    window = Screen()
    window.setup(1100, 800)
    window.bgcolor("black")
    window.title("Turtle Race")

    # Draw a gray background
    grawTurtle = Turtle()
    grawTurtle.hideturtle()
    grawTurtle.color("gray")
    grawTurtle.speed("fastest")
    grawTurtle.penup()
    grawTurtle.goto(-550, -400)
    grawTurtle.begin_fill()
    grawTurtle.forward(930)
    grawTurtle.left(90)
    grawTurtle.forward(800)
    grawTurtle.left(90)
    grawTurtle.forward(930)
    grawTurtle.left(90)
    grawTurtle.forward(800)
    grawTurtle.end_fill()

    # Draw the white finish line
    whiteTurtle = Turtle()
    whiteTurtle.hideturtle()
    whiteTurtle.pencolor('white')
    whiteTurtle.penup()
    whiteTurtle.goto(380,-400)
    whiteTurtle.pendown()
    whiteTurtle.left(90)
    whiteTurtle.pensize(20)
    whiteTurtle.forward(800)
    whiteTurtle.penup()
    whiteTurtle.home()
    whiteTurtle.pendown()

    # For writing text
    wrinting_turtle = Turtle()
    wrinting_turtle.hideturtle()

    colors = ('red','blue','green')
    y_positions = (-250,0,250)
    turtles = []

    for i in range(3):
        new_turtle = Turtle('turtle') 
        new_turtle.shapesize(2)
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-500, y_positions[i])
        turtles.append(new_turtle)

    def check_result():
        "Check if one of the three turtles is crossing the white finish line"
        for turtle in turtles:
            if turtle.xcor() > 380:
                return turtle.pencolor()

    def display_result(guessing, winner):
        "Display the final results"
        window.clear()
        window.bgcolor('DeepPink')
        if guessing == winner:
            whiteTurtle.write("You win!", align= "center", font= ("Arial", 40, "bold"))
            mixer.music.load(r"win_sound.mp3")
        else:
            whiteTurtle.write("You Lose!", align= "center", font= ("Arial", 40, "bold"))
            mixer.music.load(r"lose_sound3.mp3")
        mixer.music.play()
        time.sleep(2)


    is_race_on = True
    while is_race_on:
        guessing = window.textinput("Make your bet", "Guess the winner: \nType a color: Red, Blue or Green ?").lower()
        if guessing in ["blue", "red", "green"]:
            mixer.music.load(r'starting_game_sound.mp3')  
            mixer.music.play()
            time.sleep(3)
            mixer.music.load(r'exiting_match_sound.mp3')
            mixer.music.play()
        elif guessing == 'exit':
            quit()
        else:
            wrinting_turtle.color("orange")
            wrinting_turtle.write("Invalid Choice", align= "center", font= ("Arial", 30, "bold"))
            time.sleep(2)
            wrinting_turtle.clear()
            continue

        while True:
            for turtle in turtles:
                turtle.forward(random.randint(1,8))
                winner = check_result()
            if winner:
                wrinting_turtle.color("green")
                display_result(guessing, winner)
                is_race_on = False
                break
                

while True:
    game()
    time.sleep(2)
