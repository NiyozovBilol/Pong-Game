from turtle import Turtle


class ComputerPaddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(350, 0)
        self.go_forward = True
        self.go_backward = False

    def move(self):
        if self.go_forward:
            self.forward(10)
            if self.ycor() > 260:
                self.go_forward = False
                self.go_backward = True
        elif self.go_backward:
            self.backward(10)
            if self.ycor() < -260:
                self.go_forward = True
                self.go_backward = False
