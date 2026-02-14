#TurtleGraphics.py
#Name:Devyn Conaway
#Date:2/14/26
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(annith, sides):
    for s in range(sides):
        annith.forward(100)
        annith.right(360/sides)

def fillCorner(sybella, corner):
    drawSquare(sybella, 200)
    if corner == 1:
        sybella.begin_fill()
        drawSquare(sybella, 100)
        sybella.end_fill()
    if corner == 2:
        sybella.forward(100)
        sybella.begin_fill()
        drawSquare(sybella, 100)
        sybella.end_fill()
    if corner == 3:
        sybella.right(90)
        sybella.forward(100)
        sybella.left(90)
        sybella.begin_fill()
        drawSquare(sybella, 100)
        sybella.end_fill()
    if corner == 4:
        sybella.forward(200)
        sybella.right(90)
        sybella.forward(100)
        sybella.begin_fill()
        drawSquare(sybella, 100)
        sybella.end_fill()

def squaresInSquares(ismae, num):
    startSquare = 25
    for i in range(num):
        drawSquare(ismae, startSquare)
        startSquare += 40
        ismae.up()
        ismae.backward(20)
        ismae.left(90)
        ismae.forward(20)
        ismae.right(90)
        ismae.down()
    

def main():
    myTurtle = turtle.Turtle()
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    
    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares

main()
