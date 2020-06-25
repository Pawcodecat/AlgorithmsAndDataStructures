from collections import deque
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

DAG = [[1,7], [2,7], [5], [2,4],[5], [], [7],[],[]]


topological_sorted = []
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
    topological_sorted.insert(0, u)







if __name__ == '__main__':
    dfs_list(DAG)
    print(topological_sorted)






















