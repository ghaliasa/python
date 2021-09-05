import turtle
# jojo
# jojo
window = turtle.Screen()
window.title("mouayad ping pong")
window.bgcolor("purple")
window.setup(450, 450)
window.tracer(0)
x = 0
m1 = turtle.Turtle()

m1.setx(x)
m1.shape("circle")
m1.color("red")
m1.goto(100, 100)
m1.penup()

koko = True


def aa():
    i = 100000
    koko = False
    print("aaaaaa")


i = 0
window.listen()
window.onkeypress(aa(), "w")
while koko:
    x += 1
    i += 0.0001
    m1.speed(x)
    window.update()
