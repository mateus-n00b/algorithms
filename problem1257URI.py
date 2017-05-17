
alpha = {
'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,
'G':6,'H':7,'I':8,'J':9,'K':10,
'L':11,'M':12,'N':13,'O':14,'P':15,
'Q':16,'R':17,'S':18,'T':19,'U':20,
'V':21,'W':22,'X':23,'Y':24,'Z':25}

t = int(raw_input())
words = []
out = []
soma = 0
for i in xrange(t):
    n = int(raw_input())
    for j in xrange(0,n):
        words = raw_input()
        for k in range(0,len(words)):
            soma += alpha[words[k]]+k+j            
    out.append(soma)
    soma = 0
for x in out:
    print x
