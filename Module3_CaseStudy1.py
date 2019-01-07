
############################################
#Module3_CaseStudy1
##############################################

#1.

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

##############################################
#6. 

for x in range(2000,3001):
    if x%7==0 and x%5!=0 :
        print(x  , end= ',')

##############################################
