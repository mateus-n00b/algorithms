# Code for the cutting rod problem.
# Adapted from Cormen's book.
#
# Coded by Mateus Sousa
def bottom_up(p,n):
    r = [ 0 for i in range(n+1)]
    r[0] = 0
    for i in range(1,n+1):
        q = -32767
        for j in range(i):
            q = max(q,p[j]+r[i-j-1])
        r[i] = q
    return r[n]

pi = map(int,raw_input().split(' '))
print bottom_up(pi,len(pi))
