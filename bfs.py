#!/usr/bin/env python
# Performs a breadth-first search on a graph

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop()
    def isEmpty(self):
        return len(self.queue) != 0

def doBFS(graph,source):
    queue = []
    bfsInfo = []
    distance = 0;
    for i in range(0,len(graph)):
        bfsInfo.append({'distance':None, 'predecessor':None})

    bfsInfo[source]['distance'] = distance
    queue = Queue()
    queue.enqueue(source)

    while queue.isEmpty():
        u = queue.dequeue()
        for i in range(0,len(graph[u])):
            v = graph[u][i]
            if bfsInfo[v]['distance'] == None and v != source :
                queue.enqueue(v)
                bfsInfo[v]['distance'] = bfsInfo[u]['distance']+1
                bfsInfo[v]['predecessor'] = u

    return bfsInfo

adjList = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []]

bfsInfo = doBFS(adjList, 3)

for i in range(0,len(adjList)):
    print "vertex %d distance = %s predecessor = %s" % (i,str(bfsInfo[i]['distance']),str(bfsInfo[i]['predecessor']))
