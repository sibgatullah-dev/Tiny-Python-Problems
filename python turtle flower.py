from turtle import *
import colorsys

speed(0)
bgcolor("black")
a = 0
for i in range(16):
    for j in range(24):
        c= colorsys.hsv_to_rgb(a, 1, 1)
        color(c)
        a += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)
done()