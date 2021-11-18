# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:46:05 2021

@author: javia
"""
from math import ceil, floor

class Solution:

    def number_prediction(self, input):
        # Your code goes here
        output=input #In case I don't want to modify the input
        while '_' in output:
            position=output.index('_')
            past=output[:position]
            if not past:
                output='0'+output[position+1:]
            else:
                output=self.find_match(past)+output[position+1:]
                
        return output
            #when the dash is on the second position, just repeat the first element. 
            #This case can be identified with not finding a match at any point of the search and you return the last element of the past (different of finding a match of a given length and then not being able to find a match of greater length)
            #II the dash is in the first position, add 0
            #I could stop searching for greater matches when the lengh surpasess half of the length of the past
    
    #Review why it is not working for the long string tests
    def find_match(self,past)->str:
        #returns the the past + next character
        l=1
        next_char=past[-1]
        string_to_match=past[-1]
        substring=past[:-1]
        while l<=ceil(len(past)/2) and l<11:  #I think I should use floor because I am looking to match a string of length l+1. If I use ceil, I would try to search strings of length precisly ceil(), but that is never going to give the right answer
            #to make it a bit more efficient, instead of computing the tail every time, we are just going to add the new element
            if string_to_match in substring:
                #to compute the last position of the string_to_match in substring I compute the first position of reverse in reverrse 
                reverse_substring=substring[::-1]
                reverse_to_match=string_to_match[::-1]
                reverse_max_position=reverse_substring.index(reverse_to_match)
                #the position of a substring of lenght l in a string of length n, provided that the position of reverses is p is given by:
                    #n-l-p
                #max_position=len(substring)-reverse_max_position-len(string_to_match) #I may leave out the lengh of the string_to_match because I will look for the character after it
                search_position=len(substring)-reverse_max_position
                next_char=past[search_position] #I search it in past because it can be an element in the tail
                string_to_match=past[-l-1]+ string_to_match
                substring=substring[:-1]
                l+=1
            else:
                break
            
        return past+next_char
            
            
            
        
    