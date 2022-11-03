import turtle

t = turtle.Turtle()

t.forward(1)

while True:
    distance = t.distance(0,0)
    t.forward(100/distance)