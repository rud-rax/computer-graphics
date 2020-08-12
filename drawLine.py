#!/usr/bin/env python3

import sys
#import datetime
import dda_line_drawing_algo as lineAlgo

pixels = {'x' : 50 , 'y' : 50 , 'fill' : ".", 'linefill' : 'X'}

def checkBoundaries(point_list):
    isCrossing = False
    for x,y in point_list:
        if x > pixels['x'] or y > pixels['y']:
            isCrossing = True
    return isCrossing

filename = r"line"

def draw(filename,point_list):
    #point_list = lineAlgo.dda_algorithm()

    with open(filename,"w") as drawfile:
        for r in range(0,pixels['x']):
            for c in range(0,pixels['y']):
                if (r,c) in point_list:
                    drawfile.write(pixels['linefill'])
                else :
                    drawfile.write(pixels['fill'])
            drawfile.write('\n')

if __name__ == "__main__":
    point_list = lineAlgo.dda_algorithm()
    draw(filename,point_list)
    sys.exit(0)
