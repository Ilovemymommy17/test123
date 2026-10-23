from turtle import *
import coloursys

bgcolor('black')
pensize(2)
tracer(10)
h=0

colores = ['white', '#ffcb7d', '#FFA216']

def dibujo(a,n):
    circle(5+n,60), left(a), circle(5+n,60)

    for i in range(360):

        color_index = (i // 15) % 3
        c = colores[color_index]
        color(c,'black'), begin_fill()
        dibujo(90,i/2), end_fill()
        dibujo(0,0), dibujo(90,i/2), pendown()

        done()