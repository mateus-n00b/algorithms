def bSearch(array,p,q,value):
    if q >= p:
        a = (q+p)/2
        if array[a] == value:
            return a
        elif array[a] > value:
            return bSearch(array,p,a-1,value)
        else:
            return bSearch(array,a+1,q,value)
    else:
        return -1


array = [20,25,37,41,58,60]
p = 0
q = len(array)-1
print bSearch(array,p,q,0)
