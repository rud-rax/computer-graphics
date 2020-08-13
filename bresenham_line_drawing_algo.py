#!/usr/bin/env python3

import sys
import dda_line_drawing_algo as lineAlgo



def bresenham_algorithm(points):
    point_list = []

    # STEP 1
    #points = lineAlgo.inputPointValues()
    p1 = lineAlgo.Point(points[0],points[1])
    p2 = lineAlgo.Point(points[2],points[3])

    # STEP 2
    dx = p2.x - p1.x
    dy = p2.y - p1.y

    if abs(dx) > abs(dy) :
        steps = abs(dx)
    else :
        steps = abs(dy)

    # STEP 3
    x,y = p1.x,p1.y
    pk = (dy*2) - dx
    print("| x | y |")
    print("-"*9)
    for _ in range(0,steps+1):
        point_list.append((x,y))
        print("|" + str(x).center(3)+"|"+str(y).center(3)+"|")
        if pk >= 0 :
            pk = pk + (2*dy) - (2*dx)
            x += 1
            y += 1
        else :
            pk = pk + (2*dy)
            x += 1


    return point_list


if __name__ == "__main__":
    points = lineAlgo.inputPointValues()
    point_list = bresenham_algorithm(points)
    #print(point_list)
    sys.exit(0)
