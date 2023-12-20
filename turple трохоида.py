#трохоида
import math
from turtle import *


hideturtle()

pencolor("white")
setpos(200,0)

R = 15
r_sm = 8
m = r_sm / R
h = 10
st = 15000


for i in range(0,st,10):
    speed(9)
    pencolor("black")
    pensize(2)
    if i==0:
        pencolor("white")
    else:
        pencolor("blue")
    xx = int(7*(R * (m + 1) * math.cos(m * i / 57.29) - h * math.cos((m + 1) * i / 57.29)))
    yy = int(7*(R * (m + 1) * math.sin(m * i / 57.29) - h * math.sin((m + 1) * i / 57.29)))
    setposition(xx,yy)

exitonclick()