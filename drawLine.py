#!/usr/bin/env python3

import sys
#import datetime
import dda_line_drawing_algo as ddaLineAlgo
import bresenham_line_drawing_algo as bresenhamLineAlgo

pixels = {'x' : 50 , 'y' : 50 , 'fill' : "O", 'linefill' : ' '}

def checkBoundaries(point_list):
    isCrossing = False
    for x,y in point_list:
        if x > pixels['x'] or y > pixels['y']:
            isCrossing = True
    return isCrossing

filename = r"line"

def draw(filename,point_list):

    with open(filename,"w") as drawfile:
        for c in range(0,pixels['x']):
            for r in range(0,pixels['y']):
                if (r,c) in point_list:
                    drawfile.write(pixels['linefill'])
                else :
                    drawfile.write(pixels['fill'])
            drawfile.write('\n')

if __name__ == "__main__":
    point_list = []
    number_of_lines = int(sys.argv[1])
    default_algo = "D"
    if sys.argv[2]:
        selected_algo = sys.argv[2]
    else : selected_algo = default_algo

    if selected_algo :
        if selected_algo == "D" :
            for i in range(1,number_of_lines+1):
                print(f"LINE {i} : ")
                point_list += ddaLineAlgo.dda_algorithm(ddaLineAlgo.inputPointValues())
        if selected_algo == "B" :
            for i in range(1,number_of_lines+1):
                print(f"LINE {i} : ")
                point_list += bresenhamLineAlgo.bresenham_algorithm(ddaLineAlgo.inputPointValues())

    if not checkBoundaries(point_list):
        draw(filename,point_list)
        sys.exit(0)
    else : sys.exit(1)
