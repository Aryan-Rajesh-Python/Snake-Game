from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        turtle1=Turtle("square")
        turtle1.color("white")
        turtle1.penup()
        turtle1.goto(position)
        self.segment.append(turtle1)
    def extend(self):
        self.add_segment(self.segment[-1].position())
    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            seg_1=self.segment[seg-1].xcor()
            seg_2=self.segment[seg-1].ycor()
            self.segment[seg].goto(seg_1,seg_2)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)