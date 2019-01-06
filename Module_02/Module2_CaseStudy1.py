# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 23:42:06 2018

@author: Sudarshan
"""

###################################################
#Module2_CaseStudy1
#1.Write a program which will find factors of given number and find whether the factor is even or odd

number = int(input("Enter number  : "))

print('Factors : ')

for num in range(1,number+1):
    if number%num == 0 :
        print(num ,end = " ")
        if num%2 == 0 :
            print("is Even")
        else:
            print("is Odd")


####################################################
#Module2_CaseStudy1
#2.Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically


input_str = input("Enter words: ")

words_list = input_str.split()

words_list.sort()

for word in words_list:
    print(word,end=' ')
    
####################################################
#Module2_CaseStudy1
#3.Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line


for number in range(1000,3001):
    my_str = str(number)
    
    allEven = True
    
    for s in my_str:
        if int(s)%2 !=0:
            allEven = False
            break
        else:
            pass
    if allEven : print(number,end=',')
    
    
###############################################
#Module2_CaseStudy1
#4.Write a program that accepts a sentence and calculate the number of letters and digits

in_str = input("Enter string  : ")  
    
letters = 0
digits = 0

for character in in_str :
    if character.isdigit():
        digits+=1
    elif character.isalpha():
        letters +=1
    else:
        pass

print("Letters in input string : ", letters)
print("Digits in input string  : ", digits)

##################################################
#Module2_CaseStudy1
#5.Design a code which will find the given number is Palindrome number or not

user_str = input("Enter number : ")


if not user_str.isdecimal():
    print("Not a number")
elif len(user_str) == 1:
    print("Can't determine Palindrome for single digit")
else:
    rev_user_str = user_str[::-1]
    if rev_user_str == user_str : print(user_str, " is Palindrome!!!")
    else : print(user_str, "is not a Palindrome!!!")