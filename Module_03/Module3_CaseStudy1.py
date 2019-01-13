# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:01:06 2019

@author: Sudarshan
"""
##################################################################

#Module 3: Deep Dive -Functions, OOPs, Modules,Errors andExceptions
#Case Study 1
####################################################################


####################################################################
#1. A Robot moves in a Plane starting from the origin point (0,0). 
#The robot can move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:UP 5 DOWN 3 LEFT 3 RIGHT 2 The numbers after directions are steps.  
#Write a program to compute the distance current position after sequence of movements

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
#2. Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
def linSearch(item,my_list):
    is_found = False
    position = 0
    while position < len(my_list) and not is_found:
        if my_list[position] == item:
            is_found = True
        position = position + 1
    return is_found


#assuming sorted list from XYZ
sorted_list_XYZ = ['a','b','c','d','e','f']

item = input('What item do you want to search? : ')

itemFound = linSearch(item,sorted_list_XYZ)

if itemFound:
    print('Yes, the item is in the list')
else:
    print('No, the item is NOT in the list')
    
##############################################
#3.Weather forecasting organization wants to show is it day or night. So, write a program for such organization to findwhether is it dark outside or not
import time

print(time.ctime()) # 'Mon Oct 18 13:35:29 2010'
hour,minute,am_pm = time.strftime('%H,%M,%p').split(',')

#Assuming it gets dark at 1800 and stays dark until 0600 

if int(hour) >= 18 or int(hour) < 6 :
    print("---Night time. Its Dark Outside---")
elif int(hour) < 18 or int(hour) >= 6 :
    print("---Day time. Its not Dark outside---")


##############################################
#4. Write a program to find distancebetween two locations when their latitude and longitudes are given
from math import sin, cos, sqrt, atan2, radians

lat1 = radians(float(input("Input Latitute 1 : ")))
lat2 = radians(float(input("Input Latitute 2 : ")))
lon1 = radians(float(input("Input Longitude 1: ")))
lon2 = radians(float(input("Input Longitude 2: ")))

R = 6373.0      #approx radius of earth km 

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("\nResult:", distance) 
##############################################
#5.Design a software for bank system. There should be options like cash withdraw, cash credit and change password. According to user input, the software should provide required output.
amount = 1000.00    #Assuming initial amount = 1000.00 Rs   
password = '1234'   #assuming initial password 
exit_input = ''

def cash_withdraw():
    global amount 
    toGive = float(input("Amount to withdraw : "))
    if toGive > amount:
        print("Can't dispence more than available amount.")
    elif toGive <= amount :
        amount = amount - toGive
        print ("Collect money")
        print("Available amount : Rs.",amount )

def cash_credit():
    global amount
    toCredit = float(input("Amount to credit : "))
    if toCredit <=  0.00:
        print("Can't creadit this amount.")
    else :
        amount = amount + toCredit
        print ("Credit Done")
        print("Available amount : Rs.",amount )

def change_pwd():
    global password 
    newPwd1 = int(input("Enter new 4 digit password : "))
    newPwd2 = int(input("Enter new 4 digit password : "))
    if len(str(newPwd1)) == 4 and len(str(newPwd2)) == 4 and newPwd1 == newPwd2:
        password = str(newPwd1)
        print("Password change successful")
    else:
         print("Password change Unsuccessful")

while (exit_input !='N' and exit_input !='n' ):
    enter_pwd = int(input("Enter your 4 digit password : "))
    if str(enter_pwd) == password : 
        choice = int(input("Enter your option : \n1. Cash Withdraw \n2. Cash Credit \n3. Change password \n"))
        if choice == 1:
            cash_withdraw()
        elif choice == 2:
            cash_credit()
        elif choice == 3 : 
            change_pwd()
        else : 
            print("Invalid Choice")
    else:
        print("Wrong password")
    exit_input = input ("Press N to exit, any key to continue")
    
print("Thanks for using")


##############################################
#6. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

outlist = [x for x in range(2000,3001) if x%7==0 and x%5!=0]
print(*outlist , sep = ',')

##############################################
#7.Write a program which can compute the factorial of a given numbers. Use recursion to find it.
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
#8. Write a program that calculates and prints the value according to the given formula:Q = Square root of [(2 * C * D)/H]Following are the fixed values of C and H: C is 50. H is 30.D  is  the  variable  whose  values  should  be  input  to  your  program  in  a  comma-separated sequence
import math
d = input()
dlist = d.split(',')
def calc_formula(d):
    C = 50
    H = 30
    return math.sqrt((2*C*int(d))/H)

out = [int(calc_formula(x)) for x in dlist]
print(*out , sep = ',')

##############################################
#9. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.Note: i=0,1.., X-1; j=0,1,¡-Y-1
row = int(input("Row number : "))
col = int(input("Coloumn number : "))

d2_list =  [[i*j for j in range(col)]for i in range(row)]

print(d2_list)

##############################################
#10 . Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically
myStr = input("Enter String: ")
myStr_list = myStr.split(',')
myStr_list.sort()
print(*myStr_list,sep = ',')

##############################################
#11. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
multi_line = []
while True:
    line = input()
    if line:
        multi_line.append(line.upper())
    else:
        break;

for l in multi_line:
    print(l)
##############################################
#12. Write a program that accepts a sequence of whitespace separated words as input and   prints   the   words   after   removing   all   duplicate   words   and   sorting   them alphanumerically
myStr = input("Enter String: ")
myStr_list = myStr.split()  
myStr_list = list(set(myStr_list))
myStr_list.sort()
print(*myStr_list, sep = ' ')

#######################################
#13.  Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary numbers  as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not.  The numbers that are divisible by 5 are to be printed in a comma separated sequence

def bin_2_dec(n):
    return int(n,2)

in_str = input("Enter the num's: ") 
in_list = in_str.split(',')
out_list = [x for x in in_list if bin_2_dec(x)%5 ==0]
print(*out_list, sep = ',')

#######################################
#14. Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case letters and lower case letters.
myStr = input("Input String: ")
lower = 0
upper = 0
 
myStr_list = list(myStr)
for c in myStr_list:
    if c.isupper():
        upper = upper + 1
    elif c.islower():
        lower = lower + 1
    else : 
        pass

print("UPPER CASE ", upper)
print("LOWER CASE ", lower)

#######################################
#15. Give example of fsum and sum function of math library.


import math
 
i =  [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

print(sum(i))           #add all elements of i
print(sum(i,5))         #add all elements of i to 5 
print(math.fsum(i))     #add all elemnts of i with higher floating point precision

#######################################



















