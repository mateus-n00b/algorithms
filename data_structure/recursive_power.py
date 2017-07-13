#!/usr/bin/env python

def power(x,n):
    x = float(x)
    n = float(n)
    if n == 0:
        return 1
    if n < 0:
        return 1/power(x,-n)
    elif n%2 == 0:
        y = power(x,n/2)
        return y*y
    else:
        return x * power(x,n-1)

print power(3,-1)
