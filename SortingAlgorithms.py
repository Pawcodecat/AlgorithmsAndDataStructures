import sys

def bubble_sort(array):
    n=len(array)
    for i in range(n-1):
        print(f"line {i+1}")
        flag = False
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
            print(array)
        if(flag == False):
            break
            

def insertion_sort(arr):
    n = len(array)
    for i in range(1,n):
        j = i-1
        insert_element = arr[i]
        while(arr[j] > insert_element and j >= 0 ):
            arr[j+1] = arr[j]
            j = j - 1
        j = j + 1
        arr[j]=insert_element


def selection_sort(arr):
    n = len(arr)
    min_index = 0
    for i in range(n):
        min_value = sys.maxsize
        for j in range(i,n):
            if(arr[j] < min_value):
                min_value = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def binary_search(arr, n):
    l = 0
    r = len(arr)
    while(l <= r):
        cent = (l + r) // 2
        if(n == arr[cent]):
            return cent
        elif(n > arr[cent]):
            l = cent + 1
        else:
            r = cent - 1
    return -1


def ternary_search(arr, n):
    l = 0
    r = len(arr)

    while(l <= r):
        lcent = l + (r - l) // 3 
        rcent = r - (r - l) // 3
        if(n == arr[lcent]):
            return lcent
        elif(n == arr[rcent]):
            return rcent
        elif(n < arr[lcent]):
            r = lcent - 1
        elif(n > arr[rcent]):
            l = rcent + 1
        
        else:
            l = lcent + 1
            r = rcent -1

      
    return -1
           


def return_sorted_array():
    arr = []
    for i in range(100):
        arr.append(3 * i)
    return arr



if __name__ == "__main__":

    array = [5,2,7,4,3,9,0,1,8,6]
    array2 =[9,8,7,6,5,4,3,2,1,0]
    sorted_arr = return_sorted_array()
    print(sorted_arr)
    #print(array)
    #bubble_sort(array)
    #insertion_sort(array2)
    #selection_sort(array)
    print(f"{ternary_search(sorted_arr, 57)}")
    #print(array)