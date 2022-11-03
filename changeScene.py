from graphics import Circle,Oval,Polygon,GraphWin,Text,Point

def main():

    
    win = GraphWin('Draw a Hat for him!', 350, 350) #define window size
    win.yUp() #define orientation

    #define background + text 
    win.setBackground('white')
    message = Text(Point(win.getWidth()/2, 40), 'Click on three points to draw a hat on his head')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)

    # head
    head = Circle(Point(175,175), 50)
    head.setFill("yellow")
    head.draw(win)

    # left eye
    eye1 = Circle(Point(160, 180), 5) 
    eye1.setFill('blue')
    eye1.draw(win)

    # right eye
    eye2 = Circle(Point(180, 180), 5) 
    eye2.setFill('blue')
    eye2.draw(win)

    # mouth 
    mouth = Oval(Point(150, 160), Point(190, 155)) 
    mouth.setFill("red")
    mouth.draw(win)

    # Get and draw three vertices of triangle for hat
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    vertices = [p1, p2, p3]

    # Use Polygon object to draw the triangle for hat
    triangle = Polygon(vertices)
    triangle.setFill('purple')
    triangle.setOutline('black')
    triangle.setWidth(4)  # width hat line
    triangle.draw(win)

    message.setText('Click anywhere to quit') # to end program
    win.getMouse()
    win.close() 

main()
