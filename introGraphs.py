#!/usr/bin/env python
# coding: UTF-8
#                       A
#                      / \
#                     B---C
#                      \  /\
#                       D---F
#                            \
#                             E
#
graph = {'A':['B','C'],
        'B':['C','D'],
        'C':['D'],
        'D':['C','F'],
        'E':['F'],
        'F':['C']
}

weights = {
'A':['B',2],
'A':['C',3],
'B':['C',4],
'D':['F',7],
'B':['D',5],
'C':['D',9],
'E':['F',6],
'F':['C',4]
}

# Exemplo tirado de
def find_path(graph, start,end,path=[] ):
    path = path+[start]

    if start == end:
        return path
    if not graph.has_key(start):
        return None

    for x in graph[start]:
        if x not in path:
            newpath = find_path(graph,x,end,path)
            if newpath: return newpath
    return None

print find_path(graph, 'A','D')

def shortestPath(graph,weights,start, end):
    soma = 0
    pPath = []
    if start == end:
        return soma
    if not graph.has_key(start):
        return None

    caminho = find_path(graph, start, end)
    pPath += [start]
    for x in caminho:
        if weights[x][0] in caminho and weights[x][0] not in pPath:
           print "%s -> %s = %d" % (x, weights[x][0], weights[x][1])
           if weights[x][1] > soma:
              pPath += [weights[x][0]]
              soma += weights[x][1]
                            
    print pPath,soma
shortestPath(graph,weights,'A','D')
