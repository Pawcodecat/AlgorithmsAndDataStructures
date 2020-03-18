import sys

class Node:
    def __init__(self, val =-1, idx =-1):
        self.val = val
        self.idx = idx

class MaxHeap:
    table=[]
    def __init__(self, max_size):
        self.table = [Node() for i in range(max_size +1)]
        self.maxSize = max_size
        self.table[0].val = 0

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def parent(self, i):
        return i//2

    def size(self):
        return self.table[0].val

    def append(self, value):
        self.table.append(Node(value))
        self.table[0].val += 1

    def swap(self,old_idx, new_idx):
        self.table[old_idx], self.table[new_idx] = self.table[new_idx], self.table[old_idx]

    def add(self,value):
        self.table[0].val += 1
        self.table[self.size()].val = value

    def heapify(self, insert_index):
        l = self.left(insert_index)
        r = self.right(insert_index)
        max = insert_index

        if l <= self.size() and self.table[l].val > self.table[max].val:
            max = l
        if r <= self.size() and self.table[r].val > self.table[max].val:
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
            self.table[0].val -= 1
            self.heapify(1)

    def insert(self, value):
        if self.size() == self.maxSize:
            return

        self.table[0].val += 1
        self.table[self.size()].val = value
        i = self.size()

        while(i > 1 and self.table[i].val > self.table[self.parent(i)].val):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract(self):
        if self.size() == 0:
            return
        max_value = self.table[1].val
        self.table[1].val = self.table[self.size()].val
        self.table[0].val -= 1
        self.heapify(1)
        return max_value

    def print(self):
        for i in range(0,200):
            sys.stdout.write(f"{self.table[i].val}, ")

class MinHeap:
    table=[]
    def __init__(self, maxSize):
        self.table = [Node() for i in range(maxSize +1)]
        self.maxSize = maxSize
        self.table[0].val = 0

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def parent(self, i):
        return i//2

    def size(self):
        return self.table[0].val

    def append(self, value):
        self.table.append(Node(value))
        self.table[0].val += 1

    def swap(self,old_idx, new_idx):
        self.table[old_idx], self.table[new_idx] = self.table[new_idx], self.table[old_idx]

    def add(self,value):
        self.table[0].val += 1
        self.table[self.size()].val = value

    def heapify(self, insert_index):
        l = self.left(insert_index)
        r = self.right(insert_index)
        max = insert_index

        if l <= self.size() and self.table[l].val < self.table[max].val:
            max = l
        if r <= self.size() and self.table[r].val < self.table[max].val:
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
            self.table[0].val -= 1
            self.heapify(1)

    def insert(self, value):
        if self.size() == self.maxSize:
            return

        self.table[0].val += 1
        self.table[self.size()].val = value
        i = self.size()

        while(i > 1 and self.table[i].val < self.table[self.parent(i)].val):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract(self):
        if self.size() == 0:
            return
        max_value = self.table[1].val
        self.table[1].val = self.table[self.size()].val
        self.table[0].val -= 1
        self.heapify(1)
        return max_value

    def print(self):
        for i in range(0,200):
            sys.stdout.write(f"{self.table[i].val}, ")

class Heap:
    def __init__(self, max_size):
        self.min_heap = MinHeap(max_size)
        self.max_heap = MaxHeap(max_size)

    def insert(self,value):
        min_heap.insert(value)
        max_heap.insert(value)


if __name__ == '__main__':

    max_heap = MaxHeap(200)
    min_heap = MinHeap(200)
    heap = Heap(200)
    for i in range(1,100):
        max_heap.insert((i**5 - 8*i**4 + 34*i**3 - 67*i*2 + 128*i -312)%100)
        min_heap.add((i ** 5 - 8 * i ** 4 + 34 * i ** 3 - 67 * i * 2 + 128 * i - 312) % 100)
        heap.insert((i ** 5 - 8 * i ** 4 + 34 * i ** 3 - 67 * i * 2 + 128 * i - 312) % 100)

    # heap.print()

    heap.max_heap.print()















