matrix = [[0 for x in range(100)] for y in range(100)]
def knapsack( index,size, weights, values):

    take = 0
    dontTake = 0
    if (matrix[index][size]!=0): #checking whether the subproblem is
        return matrix[index][size] #already calculated or not
    if (index==0):  #If the given subproblem is at leave node
        if (weights[0]<=size):
            matrix[index][size] = values[0]
            return values[0]
        else:
            matrix[index][size] = 0
            return 0
    if (weights[index]<=size):
        take = values[index] + knapsack(index-1, size-weights[index], weights, values);
    dontTake = knapsack(index-1, size, weights, values);
    matrix[index][size] = max (take, dontTake);
    return matrix[index][size];


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K

def elementKnap(K, weight, val, arr_w, arr_v): # 5, 40
    list = []

    while weight > 0:
        if(K[weight][val] != K[weight][val]):
            list.append(arr_w[weight])
            weight -= 1
            val = val - arr_v[weight]
        else:
            weight -= 1

    return list


if __name__ == '__main__':
    v = [20, 5, 10, 40, 15, 25]
    w = [1, 2, 3, 8, 7, 4]
    print(knapsack(5,10,w,v)) #5=6-1,  10 = weight

    print(elementKnap(knapSack(v, w, 6, 10), 5, 40, w, v))