import sys


MATRIX = [[0,0,0,1,0],[1,0,1,0,0 ],[1,0,0,0,1],[0,0,1,0,0],[0,0,0,1,0]]
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
class Node:
    def __init__(self, distance, parent, color):
        self.distance = distance
        self.parent = parent
        self.color = color

class MinHeap:
    table=[]
    def __init__(self, maxSize):
        self.table = [Node(1000, None, "white") for i in range(maxSize +1)]
        self.maxSize = maxSize
        self.table[0].distance = 0

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def parent(self, i):
        return i//2

    def size(self):
        return self.table[0].distance

    # def append(self, value):
    #     self.table.append(Node(value))
    #     self.table[0].distance += 1

    def swap(self,old_idx, new_idx):
        self.table[old_idx], self.table[new_idx] = self.table[new_idx], self.table[old_idx]

    def add(self,value):
        self.table[0].distance += 1
        self.table[self.size()].distance = value

    def heapify(self, insert_index):
        l = self.left(insert_index)
        r = self.right(insert_index)
        max = insert_index

        if l <= self.size() and self.table[l].distance < self.table[max].distance:
            max = l
        if r <= self.size() and self.table[r].distance < self.table[max].distance:
            max = r

        if max != insert_index:
            self.swap(max, insert_index)
            self.heapify(max)

    def build_heap(self):
        for i in range(self.size() // 2, 0, -1):
            self.heapify(i)

    def heap_sort(self):
        size = self.size()
        self.build_heap()
        for i in range(size, 0, -1):
            self.swap(i, 1)
            self.table[0].distance -= 1
            self.heapify(1)

    def insert(self, node):
        if self.size() == self.maxSize:
            return

        self.table[0].distance += 1
        self.table[self.size()] = node
        i = self.size()

        while(i > 1 and self.table[i] < self.table[self.parent(i)][0]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract(self):
        if self.size() == 0:
            return
        min_node = self.table[1]
        self.table[1] = self.table[self.size()]
        self.table[0].distance -= 1
        self.heapify(1)
        return min_node

    def print(self):
        for i in range(0,self.maxSize + 1):
            sys.stdout.write(f"{self.table[i]}, ")


def print_matrix():
    for i in range(5):
        for j in range(5):
            print(MATRIX[i][j], end = ' ')
        print()

def BFS():
    minHeap = MinHeap(4)
    node_arr = []
    for i in range(0,4):
        node = Node(float("inf"), None, "white")
        node_arr.append(node)

    node_arr[0] = (0, None, "gray")
    for i in range(0, 4):
        minHeap.insert(node_arr[i])
    minHeap.print()

if __name__ == '__main__':
    BFS()



