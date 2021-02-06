# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:22:07 2021

@author: epits
"""
#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s=input()
counter=0
for i in range(0,len(s)):
    if s[i:i+3]=='bob':
        counter+=1
print('Number of times bob occurs is: '+str(counter))