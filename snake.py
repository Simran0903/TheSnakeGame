from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
RIGHT=0
DOWN=270
LEFT=180
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.head=self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.goto(position)
        turtle.color("white")
        self.turtles.append(turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())
    def move(self):
        for seg in range(len(self.turtles) - 1, 0, -1):
            newx = self.turtles[seg - 1].xcor()
            newy = self.turtles[seg - 1].ycor()
            self.turtles[seg].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
