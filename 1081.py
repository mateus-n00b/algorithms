#!/usr/bin/env python
# DFSr - Depth Hierarchy
# Mateus Sousa (n00b)
# June 2017
#
# https://www.urionlinejudge.com.br/judge/en/problems/view/1081
# 

visited = []
space = "  "
temp = ""
def dfs(G,s):
    global space
    global temp
    ts = space
    visited.append(s)
    for n in G[s]:
        if n not in visited:
               print ts+"%d-%d pathR(G,%d)" % (s,n,n)
               space +="  "
               dfs(G,n)
        else:
            print ts+"%d-%d" % (s,n)
        space = ts
    ts = "  "

def fill(G,v):
    for j in range(0,v):
        G.append([])
    return G

G = []

n = int(raw_input())
for k in range(n):
    key = True
    v, e = raw_input().split(' ')
    v,e = int(v),int(e)
    G = fill(G,v)

    for j in range(e):
        aux = raw_input().split(' ')
        v,w = int(aux[0]),int(aux[1])
        G[v].append(w)
        G[v].sort()

    print "Caso %d:" % (k+1)
    for i in range(0,len(G)):
        if i not in visited:
            dfs(G,i)
            if key:
                print
                key = False
            else:
                key = True
        elif i in visited and key:
            print
            key = False
    G = []
    visited = []
