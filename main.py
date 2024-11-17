from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet","Which turtle would win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
x_coord = -230
y_coord = 170
all_turtles = []
for i in range(6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.goto(x=x_coord,y=y_coord)
    y_coord -= 65
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning turtle is:{winning_color}")
            else:
                print(f"You lost. The winning turtle is:{winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()