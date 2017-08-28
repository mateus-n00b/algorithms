parent = {}
def DFS_visit(G,v):
    global parent

    for u in G[v]:
        if u not in parent:
            parent[u] = v
            DFS_visit(G,u)

def DFS(G):
    global parent
    for v in xrange(len(G)):
        if v not in parent:
            parent[v] = None
            DFS_visit(G,v)
    return parent

def main():
    G = [
    [1,2],
    [0,2,4],
    [0,1,4],
    [4],
    [1,2,3]
    ]
    print DFS(G)

if __name__ == '__main__':
    main()
