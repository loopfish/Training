import turtle as t
import time

t.color("blue")
t.begin_fill()

counter = 0

while counter < 4:
    t.forward(100)
    t.left(90)
    counter = counter+1
t.end_fill()

t.color("yellow")
t.begin_fill()

counter = 0

while counter < 4:
    t.forward(100)
    t.right(90)
    counter = counter+1
t.end_fill()

t.color("yellow")
t.begin_fill()

counter = 0

while counter < 4:
    t.left(90)
    t.forward(100)
    counter = counter+1

t.end_fill()

t.color("blue")
t.begin_fill()

counter = 0

while counter < 4:
    t.right(90)
    t.forward(100)
    counter = counter+1

t.end_fill()

time.sleep(10)
