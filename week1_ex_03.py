# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:28:56 2021

@author: epits
"""

#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc

s=input()
longest=''
for i in range(0,len(s)):
    current_longest=s[i]
    curr_i=i
    if (i+1) >= (len(s)-1):
        break
    while ord(s[curr_i])<=ord(s[curr_i+1]):
        current_longest+=s[curr_i+1]
        curr_i+=1
        if (curr_i+1) > (len(s)-1):
            break
        
    if len(current_longest)>len(longest):
        longest=current_longest
print('Longest substring in alphabetical order is: '+longest)