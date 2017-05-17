def swap(array, firstIndex,secondIndex ):
    aux = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = aux

def indexOfMinimum(array, startIndex):
    minValue = array[startIndex]
    minIndex = startIndex

    for i in range(minIndex+1,len(array)):
        if array[i] < minValue:
            minValue = array[i]
            minIndex = i
    return minIndex
ab = [0,1,2,3,4,5,6]
def selectioSort(array):
    for i in range(0,len(array)):
        minimo = indexOfMinimum(array,i)
        swap(array,i,minimo)
        swap(ab,i,minimo)
    print array

array = [22, 11, 99, 88, 9, 7, 42];
selectioSort(array)
print ab
