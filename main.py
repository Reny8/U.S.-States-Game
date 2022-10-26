import turtle
from numpy import empty
import pandas
#VARIABLES
screen = turtle.Screen()
background = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
#SCREEN PROPERTIES
screen.title("U.S. States Game")
screen.addshape(background)
screen.setup(width = 740, height = 500)
turtle.shape(background)
screen.bgcolor("black")

#FUNCTIONALITY
guess = screen.textinput(title = "Guess a State", prompt = "What is one of the state's name?").capitalize()
found = data[data.state == guess]

if not found.empty:
    pointer = turtle.Turtle()
    pointer.hideturtle()
    pointer.penup()
    pointer.goto(int(found.x),int(found.y))
    pointer.write(guess)
screen.exitonclick()