# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:12:00 2021

@author: epits
"""
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s=input('input:')
counter=0
for i in range (0,len(s)):
    if s[i]=='a' or s[i]== 'e' or s[i]=='i' or s[i]=='o' or s[i] =='u':
        counter+=1
    
print('Number of vows: '+str(counter))