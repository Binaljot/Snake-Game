from turtle import Turtle
import random


class Food(Turtle):  # Using Inheritance
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # Size reduced to 10 by 10
        self.color("blue")
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        # Placing the food at a random co-ordinate
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
