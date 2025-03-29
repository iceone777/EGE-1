import turtle as t
k = 15
t.up()
t.tracer(0)
for x in range(-30, 30):
    for y in range(-20, 20):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')
t.speed(5)
t.tracer(1)
t.goto(-10 * k, 10 * k)
t.down()
for i in range(7):
    t.right(90)
    t.forward(7 * k)
    t.right(90)
    t.forward(6 * k)
t.up()
t.right(90)
t.forward(3 * k)
t.right(90)
t.forward(1 * k)
t.down()
for i in range(4):
    t.right(90)
    t.forward(6 * k)
    t.right(90)
    t.forward(11 * k)