def pinta_vertice(G,v,colors):
    t = 0
    used = [-1 for i in xrange(len(colors))]

    for u in G[v]:
        if colors[u] != -1: # check if color are in use 
            used[colors[u]] = colors[u] 

    for i in xrange(len(colors)):
        if used[i] == -1: # Looks for the first available color
            colors[v] = i   # paint the vertice
            break

def colorir_grafo(G):
    t = 0
    colors = [-1 for i in xrange(len(G))] # Colors available

    for i in xrange(len(G)):    # Paint all vertices
        if colors[i] == -1:
            pinta_vertice(G,i,colors)

    used = [ 0 for i in xrange(len(colors))]

    for i in xrange(len(used)): # Return how many colors was used
        if used[colors[i]] == 0:
            used[colors[i]] = 1
            t+=used[colors[i]]


    return t,colors

def main():
    G = [
    [1,2],
    [0,2,4],
    [0,1,4],
    [4],
    [1,2,3]
    ]

    # G = [
    # [1],
    # [0]
    # ]
    # G = [
    # [1,2],
    # [0,2,3],
    # [0,1,3],
    # [1,2,4],
    # [3]
    # ]
    print colorir_grafo(G)


main()
