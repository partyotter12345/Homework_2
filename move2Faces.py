#move2Faces.py
#HMWK #2

from graphics import *
import time


def moveAll(shapeList, dx, dy):
    ''' Move all shapes in shapeList by (dx, dy).'''    
    for shape in shapeList: 
        shape.move(dx, dy)
            


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

    win = GraphWin('2 Faces', 500, 500)
    win.yUp() # make right side up coordinates!

    faceList1 = makeFace(Point(230,250),win)
    faceList2 = makeFace(Point(270,250),win)

    for i in range(46):
        moveAll(faceList1, -5, -5)
        moveAll(faceList2, 5, 5)
        time.sleep(0.1)

    win.promptClose(win.getWidth()/2, 20)




main()
