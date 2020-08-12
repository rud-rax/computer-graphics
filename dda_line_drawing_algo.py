#!/usr/bin/env python3

class Point :
    def __init__(self,x,y):
        self.x = x
        self.y = y


def inputPointValues():
    x1 = int(input("ENTER THE X COORDINATE OF POINT 1 -> "))
    y1 = int(input("ENTER THE Y COORDINATE OF POINT 1 -> "))

    x2 = int(input("ENTER THE X COORDINATE OF POINT 2 -> "))
    y2 = int(input("ENTER THE Y COORDINATE OF POINT 2 -> "))
    return x1,y1,x2,y2

#DDA ALGORITHM

def dda_algorithm():
    #STEP 1
    points = inputPointValues()
    p1 = Point(points[0],points[1])
    p2 = Point(points[2],points[3])
    getDifference = lambda x1,x2 : x2 -x1

    # STEP 2
    dx = getDifference(p1.x,p2.x)
    dy = getDifference(p1.y,p2.y)

    #STEP 3
    if abs(dx) > abs(dy) :
        steps = abs(dx)   #GENTLE SLOPE
    else :
        steps = abs(dy)   #SHARP SLOPE

    #STEP 4
    x_inc = dx/steps
    y_inc = dy/steps

    #STEP 5
    x = p1.x
    y = p1.y
    for i in range(0,steps+1):
        #putpixel( round(x) , round(y) )
        print(round(x),round(y))
        x += x_inc
        y += y_inc

if __name__ == "__main__" :
    dda_algorithm()
