#!/usr/bin/env python3 

# a simple etch-a-sketch app:
# keys: w - forward, s - backwards, a - left, d - right, c - clear 

import turtle as t 

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)
    
def turn_left():
    new_heading = tim.heading() + 10  # tim.left(10) also works 
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading() - 10  # tim.right(10) also works 
    tim.setheading(new_heading)
    
def clear():
    tim.clear() 
    tim.penup()
    tim.home()
    tim.pendown() 

screen.listen()

screen.onkey(move_forward, 'w')  # will add fun and key 
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()