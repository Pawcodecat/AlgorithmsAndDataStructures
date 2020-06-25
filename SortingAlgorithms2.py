def counting_sort(arr, k):
    n = len(arr)
    count_arr = [0 for i in range(k+1)]
    copy_arr = [0 for i in range(n)]
    for i in range(n):
        count_arr[arr[i]] += 1
    for i in range(k):
        count_arr[i+1] += count_arr[i]
    for i in range(n):
        copy_arr[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1
    for i in range(n):
        arr[i] = copy_arr[i]
    return arr


def merge(arr, l, m, r):
    n1 = m - l +1
    n2 = r -m
    larr = [0] * n1
    rarr = [0] * n2

    for i in range(n1):
        larr[i] = arr[l + i]

    for j in range(n2):
        rarr[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < len(larr) and j < len(rarr):
        if larr[i] < rarr[j]:
            arr[k] = larr[i]
            k += 1
            i += 1
        else:
            arr[k] = rarr[j]
            k += 1
            j += 1

    while i< len(larr):
        arr[k] = larr[i]
        k += 1
        i += 1

    while j < len(rarr):
        arr[k] = rarr[j]
        k +=1
        j +=1

def merge_sort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr, l , m, r)

def iterative_merge_sort(arr):
    current_size = 1

    while current_size < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:
            if left + current_size -1 < len(arr) - 1:
                mid = left + current_size -1
            else:
                mid = len(arr) - 1
            if 2*current_size + left - 1 > len(arr) - 1:
                right = len(arr) - 1
            else:
                right = 2*current_size + left -1

            merge(arr,left, mid, right)
            left = left + current_size*2
        current_size = current_size*2


def partition(arr,low,high):
    pivot = high
    i = low -1
    for j in range(low, high):
        if arr[j] <= arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]


    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return (i+1)

def insertionSort(arr):
    for i in range(1, len(arr)):
        up = arr[i]
        j = i-1
        while j>=0 and arr[j] > up:
            arr[j+1] = arr[j]
            j -= 1
        arr[j +1] = up
    return arr

def bucket_sort(x):
    arr = []
    slot_num = 10

    for i in range(slot_num):
        arr.append([])

    for j in x:
        index_b = int(slot_num*j)
        arr[index_b].append(j)

    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x

def quick_sort(arr,low,high):
    if low < high:
         pivot = partition(arr,low,high)
         quick_sort(arr,low,pivot-1)
         quick_sort(arr,pivot+1,high)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)




def heapSort(arr):
    n = len(arr)

    for i in range(int(n / 2 - 1), -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)





if __name__ == "__main__":
    array = [5, 2, 2, 20, 20, 9, 0, 1, 2, 6]
    array2 = [9, 20, 1, 6, 1, 4, 15, 1, 1, 0]
    array3 = [0.456, 0.635,0.311, 0.890, 0.231, 0.564, 0.534, 0.123, 0.456, 0.765]
    counting_sort(array,20)
    #quick_sort(array2,0,9)
    #iterative_merge_sort(array2)
    #bucket_sort(array3)
    # heapSort(array)
    print(array)


