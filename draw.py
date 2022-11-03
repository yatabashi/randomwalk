import turtle

def origin(t: turtle.Turtle, size: float):
    halfsize = size/2

    t.forward(halfsize)
    t.left(90)

    t.begin_fill()
    t.forward(halfsize)
    for _ in range(3):
        t.left(90)
        t.forward(size)
    t.left(90)
    t.forward(halfsize)
    t.end_fill()

    t.left(90)
    t.forward(halfsize)
    
    t.setheading(0)