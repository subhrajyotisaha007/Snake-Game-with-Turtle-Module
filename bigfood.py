from turtle import Turtle
from random import randint
import turtle

class BigFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('green')
        self.speed('fastest')
        self.hideturtle()

        
    def refresh(self):
        x_axis = randint(-250, 280)
        y_axis = randint(-250, 250)
        self.goto(x_axis, y_axis)
        self.hideturtle()
    def show_bigfood(self):
        self.showturtle()
        turtle.ontimer(self.hideturtle, 5000)
