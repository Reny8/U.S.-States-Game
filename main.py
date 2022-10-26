import turtle
import pandas
#VARIABLES
screen = turtle.Screen()
background = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
guessed_states = []
#SCREEN PROPERTIES
screen.title("U.S. States Game")
screen.addshape(background)
screen.setup(width = 740, height = 500)
turtle.shape(background)
screen.bgcolor("black")

#FUNCTIONALITY
while len(guessed_states) < 50:
    guess = screen.textinput(title = f"{len(guessed_states)} / 50 States Correct", prompt = "What is one of the state's name?").capitalize()
    found = data[data.state == guess]

    if not found.empty:
        guessed_states.append(guess)
        pointer = turtle.Turtle()
        pointer.hideturtle()
        pointer.penup()
        pointer.goto(int(found.x),int(found.y))
        pointer.write(guess)


# screen.exitonclick()