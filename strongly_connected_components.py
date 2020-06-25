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

def transpose_graph(G):
    size = len(G)
    Gt = [[] for i in range(size)]

    for i in range(size):
        for j in range(len(G[i])):
            Gt[G[i][j]].append(i)

    return Gt




def dfs_list(G, colors, parents, processed, finished):

    size = len(G)
    for u in range(size):
        colors.append(Color.WHITE)
        parents.append(None)
        processed.append(float('inf'))
        finished.append(float('inf'))


    for u in range(size):
        if colors2[u] == Color.WHITE:
            dfs_visit_list(G, u, colors, parents, processed, finished)

    return parents2

def dfs_visit_list(G, u, colors, parents, processed, finished):
    global time
    time += 1
    processed[u] = time
    colors2[u] = Color.GRAY
    for v in G[u]:
        if colors[v] == Color.WHITE:
            parents[v] = u
            dfs_visit_list(G, v, colors, parents, processed, finished)
    colors[u] = Color.BLACK
    time += 1
    finished[u] = time

def strongly_connected_component(G):
    dfs_list(G)
    Gt = transpose_graph(G)


if __name__ == '__main__':
    colors2 = []
    parents2 = []
    processed2 = []
    finished2 = []
    time = 0
    dfs_list(DAG, colors2, parents2, processed2, finished2)
    print(parents2)
    # dfs_list(DAG)
    # print(parents2)