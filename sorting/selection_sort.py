# Troca valor A[x] por A[y]
def swap(array, firstIndex,secondIndex ):
    aux = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = aux

# Retorna o index do menor valor do array
def indexOfMinimum(array, startIndex):
    minValue = array[startIndex]
    minIndex = startIndex

    for i in range(minIndex+1,len(array)):
        if array[i] < minValue:
            minValue = array[i]
            minIndex = i
    return minIndex

# Realiza a permutacao
def selectioSort(array):
    for i in range(0,len(array)):
        minimo = indexOfMinimum(array,i)
        # Troca o A[i] por A[minimo]
        swap(array,i,minimo)
    print array

array = [22, 11, 99, 88, 9, 7, 42];

selectioSort(array)
