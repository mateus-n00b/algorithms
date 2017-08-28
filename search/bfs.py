def BFS(G,s):
    visited = []
    level = {}
    parent = {}
    queue = []

    level[s]=0
    visited.append(s)
    parent[s] = None

    queue.append(s)

    while len(queue)!=0:
        v = queue.pop()
        for u in G[v]:
            if u not in visited:
                parent[u] = v
                level[u] = level[v]+1
                visited.append(u)
                queue.append(u)
    return level,parent


def main():
        G = [
        [1,2],
        [0,2,4],
        [0,1,4],
        [4],
        [1,2,3]
        ]
        print BFS(G,3)

if __name__ == '__main__':
    main()
