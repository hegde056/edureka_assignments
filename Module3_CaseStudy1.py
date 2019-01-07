
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

outlist = [x for x in range(2000,3001) if x%7==0 and x%5!=0]
print(*outlist , sep = ',')

##############################################
#7.
def rec_fact( n ):
    if n == 1:
        return n
    else:
        return n*rec_fact(n-1)

n =  int(input ("Enter number :"))       
if n<0 :
    print("no factorial of -ve num's")
elif n==0:
    print("Factorial of ",n," is ","1")
else:
    print("Factorial of ",n," is ",rec_fact(n))

##############################################
#8. 
import math
d = input()
dlist = d.split(',')
def calc_formula(d):
    C = 50
    H = 30
    return math.sqrt((2*C*int(d))/H)

out = [int(calc_formula(x)) for x in dlist]
print(*out , sep = ',')
