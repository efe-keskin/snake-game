from turtle import Turtle, Screen, onkey, listen

screen = Screen()
listen()
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
movement_distance = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        def move_up():
            if self.head.heading() != 270:
                self.head.setheading(90)

        def move_down():
            if self.head.heading() != 90:
                self.head.setheading(270)

        def move_right():
            if self.head.heading() != 180:
                self.head.setheading(0)

        def move_left():
            if self.head.heading() != 0:
                self.head.setheading(180)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(movement_distance)
        onkey(key="w", fun=move_up)
        onkey(key="s", fun=move_down)
        onkey(key="d", fun=move_right)
        onkey(key="a", fun=move_left)

    def add_snake(self):
        efe = Turtle()
        efe.color("white")
        efe.shape("square")
        efe.penup()
        self.segments.append(efe)
    def reset(self):
        for seg in self.segments:
            seg.goto(540,600)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
