
############################################
#Module3_CaseStudy1
##############################################

#1.A Robot moves in a Plane starting from the origin point (0,0). The robot can move 
#toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given 
#following: UP 5 DOWN 3 LEFT 3 RIGHT 2 . The 
#numbers after directions are steps.  Write a program to compute the 
#distance current position after sequence of movements.

import math

x1 = y1 = 0
rmove = input("Give Robot movement trace in signle line : ")
rmovelist = rmove.split()
dirlist = rmovelist[0::2]
dislist = rmovelist[1::2]
for a,b in zip(dirlist, dislist) :
    if a == 'UP':
        y1 = y1 + int(b)
    if a == 'DOWN':
        y1 = y1 - int(b)
    if a == 'RIGHT':
        x1 = x1 + int(b)
    if a == 'LEFT':
        x1 = x1 - int(b)


disFromOrig = math.sqrt(pow(x1,2)+pow(y1,2))

print("Distance from Origin: ", disFromOrig)
