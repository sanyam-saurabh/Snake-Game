from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):

        for position in STARTING_POSITION:
            self.add_snake_part(position)


    def move(self):
        for snake_part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake_part - 1].xcor()
            new_y = self.snake_parts[snake_part - 1].ycor()
            self.snake_parts[snake_part].goto(new_x, new_y)
        self.head .forward(20)

    def add_snake_part(self,position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)


    def extend(self):
        #add a new segment
        self.add_snake_part(self.snake_parts[-1].position())

    def up(self):
        if self.head.heading()!= DOWN:
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