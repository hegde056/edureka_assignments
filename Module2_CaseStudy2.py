# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:59:38 2019

@author: Sudarshan
"""
#################################################
#           Module 2 Case Study 2 
#
#####################################################
#1. What is the output of the following code?nums =set([1,1,2,3,3,3,4,4])print(len(nums))
#           Ans. 4

#####################################################
#2.What will be the output?d ={"john":40, "peter":45}print(list(d.keys()))
#           Ans. ['john','peter']

#####################################################
#3. A website requires a user to input username and password to register. 
#Write a program to check the validity of password given by user. 
#Following are the criteria for checking password:1. At least 1 letter between [a-z]2. At least 1 number between [0-9]1. At least 1 letter between [A-Z]3. At least 1 character from [$#@]4. Minimum length of transaction password: 65. Maximum length of transaction password: 12

password = input("Enter password : ")

uppercaseFlag = False
lowercaseFlag = False
numberFlag = False
signFlag = False

for char in password:
   if char.isupper():
       uppercaseFlag = True
   if char.islower():
       lowercaseFlag = True
   if char.isdigit():
       numberFlag = True
   if char in '$#@' : 
       signFlag = True

if (12 >= len(password) >= 6) and uppercaseFlag and lowercaseFlag and numberFlag and signFlag:
    print("Password accepted")
else:
    print("Password Not accepted")
    
#####################################################
#4.Write a for loop that prints all elements of a list and their position in the list.   

a = [4,7,3,2,5,9]
for index,element in enumerate(a):
    print('Element = ', element, ': Position = ', index)

#####################################################
#5. Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes.
#Example: If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9d Then, the output of the program should be:Helloworld

myStr = input("Input String : ")
for index,ch in enumerate(myStr):
    if index % 2 == 0:
        print(ch,end='')
        
#####################################################
#6.Please write a program which accepts a string from console and print it in reverse order.
#Example: If the following string is given as input to the program: rise to vote sir Then, the output of the program should be:ris etov ot esir

myStr = input("Input String :\t")
print("Reversed String:",myStr[::-1])

#####################################################
#7. Please write a program which count and print the numbers of each character in a string input by console  

myStr = input("Input string: ")
for item in sorted(set(myStr)):
    print(item ,',', myStr.count(item))
#####################################################
#8. With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],write   a program to make a list whose elements are intersection of the above given lists.

l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]        
print([x for x in l1 if x in l2])  
     
#####################################################
#9.By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]

in_list = [12,24,35,24,88,120,155]

out_list = [x for x in in_list if x!=24]

print(out_list)

#######################################################

#10.By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]

in_list = [12,24,35,70,88,120,155]

out_list = [x[1] for x in enumerate(in_list) if x[0]!= 0 and x[0]!= 4 and x[0]!= 5]

print(out_list)

###########################################################
#11.By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

in_list = [12,24,35,70,88,120,155]

out_list = [x for x in in_list if x%5!=0 and x%7 !=0]

print(out_list)

########################################################
#12. Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).

num = int(input("Enter integer: "))
summation = 0
for item in range (1,num+1):
    summation = summation + (item/(item+ 1))
print(summation)
########################################################

