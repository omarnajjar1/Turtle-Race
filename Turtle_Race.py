from turtle import Turtle, Screen
import random

window = Screen()
window.setup(800, 800)
window.title("Turtle Race")

sam = Turtle()
sam.shape('turtle')
sam.color('red')
sam.penup()

tom = Turtle()
tom.shape('turtle')
tom.color("blue")
tom.penup()

jan = Turtle()
jan.shape('turtle')
jan.color('green')
jan.penup()

def random_forward():
    return random.choice([2,3,4,5,6,7,8,9,10])

def check_result():
    if sam.xcor() >= 380:
        return "red"
    elif tom.xcor() >= 380:
        return "blue"
    elif jan.xcor() >= 380:
        return "green"

def display_result(guessing, winner):
    sam.pendown()  
    sam.hideturtle()
    sam.pencolor('white')
    window.clear()
    window.bgcolor('DeepPink')
    sam.home()
    if guessing.lower() == winner:
        sam.write("You win!", align= "center", font= ("Arial", 30, "bold"))
    else:
        sam.write("You Lose!", align= "center", font= ("Arial", 30, "bold"))

sam.goto(-300,-250)
tom.goto(-300,0)
jan.goto(-300, 250)

while True:
    guessing = window.textinput("Make your bet", "Guess the winner: \nType a color: Red, Blue or Green ?")
    while guessing in ["blue", "red", "green"]:
        sam.forward(random_forward())
        tom.forward(random_forward())
        jan.forward(random_forward())
        winner = check_result()
        if winner:
            display_result(guessing, winner)
            is_on_race = False
            break

    window.exitonclick()