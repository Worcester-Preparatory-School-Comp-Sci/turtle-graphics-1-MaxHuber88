import turtle
import random
import math

angle = int(input("What angle? "))
hypot = int(input("What hypotenuse? "))


boxSide = int(input("What is the side length of the box? "))


mass = int(input("What is the mass of the box? "))


x = (math.cos(math.radians(angle)))*hypot
y = (math.sin(math.radians(angle)))*hypot

turtle.hideturtle()

slope = turtle.Turtle()
slope.left(angle)
slope.forward(hypot/2)
slope.right(90+angle)
slope.forward(y)
slope.right(90)
slope.forward(x)
slope.right(180-angle)
slope.forward(hypot/2)
slope.hideturtle()

box = turtle.Turtle()
box.left(angle)
box.forward(boxSide/2)
box.left(90)
box.forward(boxSide)
box.left(90)
box.forward(boxSide)
box.left(90)
box.forward(boxSide)
box.left(90)
box.forward(boxSide/2)
box.hideturtle()


mg = turtle.Turtle()
mg.pencolor("blue")
mg.right(90)
mg.forward(mass*9.8)
mg.penup()
mg.left(90)
mg.forward(20)
mg.write(mass*9.8,)
mg.backward(20)
mg.right(90)

N = mass*9.8*math.cos(math.radians(angle))
norm = turtle.Turtle()
norm.pencolor("red")
norm.left(90+angle)
norm.forward(mass*9.8*math.cos(math.radians(angle)))
norm.write(round(N,2))
