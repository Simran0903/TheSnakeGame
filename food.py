from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("OliveDrab1")
        self.speed('fastest')   #the formation of food need not be seen
        self.shapesize(0.7,0.7)
        self.reposition()


    def reposition(self):
        randx=random.randint(-280,280)
        randy=random.randint(-280,280)
        self.goto(randx,randy)
