import numpy
def merge(A,low,high,n):
    n1 = high-low
    n2 = n-high

    i = 0
    j = 0
    # Para criar um array de tamanho fixo
    L = numpy.empty(n1, dtype=object)
    R = numpy.empty(n2, dtype=object)

    while i < n1:
        L[i] = A[low+i]
        i+=1

    while j < n2:
        R[j] = A[j+high]
        j+=1

    i = 0
    j = 0
    k = low

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1

    while i < len(L):
        A[k] = L[i]
        i+=1
        k+=1

    while j < len(R):
        A[k] = R[j]
        j+=1
        k+=1

def merge_sort(A,low,high):
    if low < high:
        mid = (low+high)/2
        # print mid
        merge_sort(A,low,mid)
        merge_sort(A,mid+1,high)
        merge(A,low,mid,high)

array = [3, 7, 12, 14, 2, 6, 9, 11]
# Res = [2,3,6,7,9,11,12,14]

merge_sort(array,0,len(array))

print array
