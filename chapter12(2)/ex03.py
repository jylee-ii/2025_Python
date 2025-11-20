import turtle

t=turtle.Pen()
t.speed(10)

t.reset()
for x in range(1,19):
    t.forward(100)
    if x%2==0:
        t.left(175)
    else:
        t.left(225)

turtle.done()