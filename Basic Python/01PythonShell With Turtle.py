x = 'hello, world'
print(x)

import random

import turtle
tao = turtle.Pen()
tao.shape('turtle')

color = ['#ff0000','#ff5e00','#fff703','#99fa07','#32fa05','#00ff7b','#00ff7b', '#00ff7b',
         '#0595fc', '#0707f5', '#7d05f5', '#d80af7','#fa05b9', '#fa05b9', '#fa0505']
color_pick = random.choice(color)

def square():
    print('square drawing')
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)

def walking(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    print('Walking to',x,y)

def RandomWalking():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    walking(x,y)
    square()

def circle():
    print('Circle')
    for i in range(0,180):
        tao.forward(i)
        tao.left(i+1)
    tao.goto(0,0)
                    
    
    

'''
square()
walking(200,200)
square()
walking(200,-200)
square()
walking(-200,0)
square()
walking(0,200)

import random
number = random.randint(0,99)
print(number)

num = random.randint(-10,10)
print(num)
'''

circle()

