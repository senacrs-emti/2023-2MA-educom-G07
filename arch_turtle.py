from turtle import *
import turtle
import math


# Ethan
class Tutel:
    def __init__(self, cateto_x, cateto_y, hip) -> None:
        self.cateto_x = cateto_y
        self.cateto_y = cateto_x
        self.hip = hip
        self.angulo_x = math.degrees(math.atan2(cateto_y, cateto_x))
        self.angulo_y = 90 - self.angulo_x

    def desenho(self) -> None:
        setup(1000,1000)
        reset()
        pensize(2)
        forward(self.cateto_x)
        left(self.angulo_x)
        begin_fill()
        color("black", "green")
        dot(10, "red")
        for i in range(3):
            forward(self.hip)
            left(90)
        dot(10, "red")
        forward(self.hip)
        end_fill()
        color("black", "blue")
        begin_fill()
        right(self.angulo_x)
        for i in range(2):
            forward(self.cateto_x)
            right(90)
        forward(self.cateto_x)
        dot(10, "red")
        end_fill()
        color("black", "red")
        begin_fill()
        for i in range(4):
            forward(self.cateto_y)
            left(90)
        end_fill()
        mainloop()
# Ethan