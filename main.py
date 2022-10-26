import turtle
from numpy import empty
import pandas
#VARIABLES
screen = turtle.Screen()
background = "blank_states_img.gif"
states = pandas.read_csv("50_states.csv")
#SCREEN PROPERTIES
screen.title("U.S. States Game")
screen.addshape(background)
screen.setup(width = 740, height = 500)
turtle.shape(background)
screen.bgcolor("black")

#FUNCTIONALITY
guess = screen.textinput(title = "Guess a State", prompt = "What is one of the state's name?")
found = states[states.state == guess.capitalize()]
if not found.empty:
    turtle.Turtle.goto (turtle.position () [found.x], turtle.position () [found.y])
    turtle.Turtle.write(found.state)

screen.exitonclick()