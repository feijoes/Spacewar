import turtle
import random
from tkinter import *

turtle.fd(0)
turtle.speed(0) 
turtle.bgcolor("black")
turtle.ht()

turtle.setundobuffer(1)
turtle.tracer(3)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1
    def move(self):
        self.fd(self.speed)
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)
    def colicion(self, other):
         if (self.xcor() >= (other.xcor() - 20)) and \
         (self.xcor() <= (other.xcor() + 20)) and \
         (self.ycor() >= (other.ycor() - 20)) and \
         (self.ycor() <= (other.ycor() + 20)):
             return True
         else:
              return False       
    
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelarate(self):
        self.speed += 1

    def decelarate(self):
        self.speed -= 1

class amigo(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 5
        self.setheading(random.randint(0,360))
    def move(self):
        self.fd(self.speed)
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)
    
class enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 5
        self.setheading(random.randint(0,360))

class Misil(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3,stretch_len=0.4, outline= None)
        self.speed = 20
        self.status = 'ready'
        self.goto(-1000, 1000)
     def fogo(self):
         if self.status == 'ready':
            self.goto(P.xcor(), P.ycor())
            self.setheading(P.heading())
            self.status = 'atirando'

     def movi(self):   
        if self.status == 'ready':
            self.goto(-1000,1000)
        if self.status == 'atirando':
            self.fd(self.speed)
        if self.xcor() < -290 or self.xcor() > 290 or self.ycor() < -290 or \
        self.ycor() > 290:
            self.status = 'ready'
            self.goto(-1000,1000)

class Game():
     def __init__(self):
       self.level = 1
       self.score = 0
       self.state = "Jogando"
       self.pen = turtle.Turtle()       
     def borda(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()
     def Score(self):
         self.pen.undo()
         msg = "Score: %s" %(self.score)
         self.pen.penup()
         self.pen.goto(-300,310)
         self.pen.write(msg, font=('Aria',16,'normal'))
game = Game()
game.borda()
game.Score()
P = Player(spriteshape="triangle", color='white', startx=0, starty=0)
Mi = Misil(spriteshape="triangle", color='yellow', startx=0, starty=0)
am = []
for a in range (6):
  am.append(amigo(spriteshape="square", color='blue', startx=100, starty=0))

enemies = []
for a in range (6):
  enemies.append(enemy(spriteshape="circle", color='red', startx=-100, starty=0))

turtle.onkey(P.turn_right, "Right")
turtle.onkey(P.turn_left, "Left")
turtle.onkey(P.accelarate, "Up")
turtle.onkey(P.decelarate, "Down")
turtle.onkey(Mi.fogo, "space")
turtle.listen()

while True:
    turtle.update()         
    P.move()
    Mi.movi()   
    for enemy in enemies:
        enemy.move()
        if  P.colicion(other = enemy ):
            y = random.randint(-250,250)
            x = random.randint(-250,250)
            enemy.goto(y,x) 
            game.score -=100
            game.Score()
        if Mi.colicion(other = enemy):
            y = random.randint(-250,250)
            x = random.randint(-250,250)
            enemy.goto(y,x)
            Mi.status = "ready"
            game.score +=100
            game.Score()
    for ally in am:
        ally.move()
        if Mi.colicion(other = ally):
            y = random.randint(-250,250)
            x = random.randint(-250,250)
            ally.goto(y,x)
            Mi.status = "ready"
            game.score -= 50
            game.Score()
        if P.colicion(other = ally):
            y = random.randint(-250,250)
            x = random.randint(-250,250)
            ally.goto(y,x)
            Mi.status = "ready"
            game.score -= 50
            game.Score()
    
    