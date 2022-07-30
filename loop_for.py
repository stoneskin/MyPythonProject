import turtle

for x in range(10):
    print("hellow "+str(x))

t = turtle.Pen()


speed = int(turtle.numinput("title","speed",10))
t.speed(speed)

for x in range(6):
    t.circle(100+10*x)
    t.left(360/6)

turtle.textinput("titile","click ok to exit")