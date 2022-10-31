#faces.py
#HMWK #2

from graphics import *
import time


def makeFace(center, win):
    '''display face centered at center in window win.
    Return a list of the shapes in the face.
    '''
    
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1Center = center.clone() # face positions are relative to the center
    eye1Center.move(-10, 5)     # locate further points in relation to others
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)

    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)

    return [head, eye1, eye2, mouth]

def main():
    win = GraphWin('Time to draw some faces!', 500,500)
    win.yUp()

    for i in range(6):
        clickpoint = win.getMouse()
        makeFace(clickpoint, win)

    win.promptClose(win.getWidth()/2, 20)
        



main()

