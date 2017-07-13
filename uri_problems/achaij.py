# Dado um array a com n elementos, encontre os indices i e j tal que a[i]+a[j] == x
#
# Mateus Sousa, Maio 2017
#
# Versao 1.0

def achaij(x, a):
    b= []
    for i in a:
        if i < x:
            b.append(i)
    for i in range(0,len(b)):
        if b[i]+b[i+1] == x:
            return True
    return False

array = [5,39,12, 4, 2]
print achaij(9, array)
