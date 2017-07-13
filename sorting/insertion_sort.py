#!/usr/bin/env python
# Just a simple implementation of the insertion sort algorithm
#
# Mateus-n00b

def insert(array,rightIndex,value):
    i = rightIndex
    while (i >= 0 and array[i] > value):
            array[i+1] = array[i]
            i-=1
    array[i+1] = value

def insertion_sort(array):
    for i in range(1,len(array)):
        insert(array,i-1,array[i])
    print array

array = [22, 11, 99, 88, 9, 7, 42]
insertion_sort(array)
