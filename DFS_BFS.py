from queue import PriorityQueue
from enum import Enum
class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


MATRIX = [[0,0,0,1,0],
          [1,0,1,0,0 ],
          [1,0,0,0,1],
          [0,0,1,0,0],
          [0,0,0,1,0]]

Graph = [[0,1,1,0],
     [0,0,0,1],
     [0,1,0,1],
     [0,0,0,0]]

G2 = [[1,2], [0,2,3], [3,1,0],[]]
MATRIX2 = [[3],[0,2],[0,4],[2],[3]]

def bfs_matrix(G,s):
    maxSize = len(G)
    parent = []
    distance = []
    colors = []

    for i in range(maxSize):
        parent.append(None)
        distance.append(float("inf"))
        colors.append(Color.WHITE)

    parent[s] = None
    distance[s] = 0
    q = PriorityQueue()
    q.put((distance[s],s))

    while not q.empty():
        u_priority = q.get()
        u = u_priority[1]
        for v in range(maxSize):
            if G[u][v] == 1 and colors[v] == Color.WHITE :
                colors[v] = Color.GRAY
                distance[v] = distance[u] + 1
                parent[v] = u
                q.put((distance[v], v))
        colors[u] = Color.BLACK

    result = []
    for i in range(maxSize):
        result.append((parent[i], distance[i]))

    return result

colors2 = []
parents2 = []
processed2 = []
finished2 = []
time = 0

def dfs_list(G):
    size = len(G)
    for u in range(size):
        colors2.append(Color.WHITE)
        parents2.append(None)
        processed2.append(float('inf'))
        finished2.append(float('inf'))


    for u in range(size):
        if colors2[u] == Color.WHITE:
            dfs_visit_list(G, u)

    return parents2

def dfs_visit_list(G, u):
    global time
    time += 1
    processed2 = time
    colors2[u] = Color.GRAY
    for v in G[u]:
        if colors2[v] == Color.WHITE:
            parents2[v] = u
            dfs_visit_list(G, v)
    colors2[u] = Color.BLACK
    time += 1
    finished2[u] = time




if __name__ == '__main__':
    # print(bfs(Graph,0))
    # print(dfs(G2))
    print(dfs_list(MATRIX2))



