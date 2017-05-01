#!/usr/bin/python
import os
#import numpy as np
#num = np.arange(301)

def doSearch(array,targetValue):
    max = len(array)-1
    min = 0
    guess = max+min/2
    while(max > min):
        
        if(array[guess] < targetValue):
            min = guess + 1
        
        elif (array[guess] > targetValue):
            max = guess-1
        else:
            return guess
        
        guess = max+min/2


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

result = doSearch(primes, 73)
print "Primo encontrado no indice " ,result
