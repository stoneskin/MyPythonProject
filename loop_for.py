import turtle

for x in range(10):
    print("hellow "+str(x))

t = turtle.Pen()
t.speed(10)

numberOfCircles = int(turtle.numinput("title","how many",20))

for x in range(6):
    t.circle(100+10*x)
    t.left(360/6)
