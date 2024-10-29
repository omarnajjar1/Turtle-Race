from turtle import Turtle, Screen
import random

# Display user's screen
window = Screen()
window.setup(1100, 800)
window.bgcolor("black")
window.title("Turtle Race")

# Make the final white line
line = Turtle()
line.hideturtle()
line.color("white")
line.penup()
line.goto(380,-400)
line.pendown()
line.left(90)
line.pensize(20)
line.forward(800)
line.speed("fastest")

# First turlte
sam = Turtle()
sam.shape('turtle')
sam.shapesize(2)
sam.color('red')
sam.penup()
sam.goto(-500,-250)

# Second turtle
tom = Turtle()
tom.shape('turtle')
tom.color("blue")
tom.shapesize(2)
tom.penup()
tom.goto(-500,0)

# Third turtle
jan = Turtle()
jan.shape('turtle')
jan.color('green')
jan.shapesize(2)
jan.penup()
jan.goto(-500, 250)

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
