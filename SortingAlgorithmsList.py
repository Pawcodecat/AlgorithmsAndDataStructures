import random

class List:
    def __init__(self):
        self.next = None
        self.val = None

def print_list(L):
    while(L != None):
        print(L.val)
        L = L.next

def bubble_sort(L):
    guard = List()
    guard.next = L
    toContinue = True
    while toContinue:
        toContinue = False
        previous = guard
        between = previous.next
        nextnode = between.next

        while nextnode != None:
            if between.val > nextnode.val:
                toContinue = True
                between.next = nextnode.next        #swap between and nextnode
                nextnode.next = previous.next
                previous.next = nextnode

                between = previous.next      #restore order previousn, between, nextnode after swap
                nextnode = between.next
            previous = previous.next        #iteration
            between = between.next
            nextnode = nextnode.next

    return guard.next
                
def selection_sort(head):
    guard = List()
    guard.next = head
    guard.min = -1
    unsorted_list_guard = guard

    while unsorted_list_guard.next != None:
        previous_node = unsorted_list_guard
        node = unsorted_list_guard.next
        previous_min = unsorted_list_guard

        while node != None:
            if node.val < previous_min.next.val:
                previous_min = previous_node

            previous_node = previous_node.next
            node = node.next

        minimum = previous_min.next
        previous_min.next = minimum.next
        minimum.next = unsorted_list_guard.next   #disconnect min from old position and connect with new position
        unsorted_list_guard.next = minimum
        unsorted_list_guard = unsorted_list_guard.next  #iteration

    return guard.next


def insertion_sort(list):
    newList = List()
    newList.next = None
    newList.val = -1
    toInsert = list

    while toInsert is not None:
        tmp = toInsert.next
        if newList.next is None:
            toInsert.next = newList.next
            newList.next = toInsert
        else:
            previous = newList
            current = newList.next

            while current is not None and current.val < toInsert.val:
                previous = previous.next
                current = current.next

            toInsert.next = current
            previous.next = toInsert

        toInsert = tmp

    return newList.next



def reverse_list(L):
    previous = L
    between = L.next
    L.next = None
    next1 = between.next
    # temp2 = temp.next
    # temp.next = L
    while (next1.next != None):
        between.next = previous  #disconnect node
        previous = between
        between = next1 
        next1 = between.next
    between.next = previous
    tail = next1
    next1.next = between
    return tail

def reverse_list2(head):
    previous = None
    nextnode = None
    while(head != None):
        nextnode = head.next
        head.next = previous  #disconnect node
        previous = head
        head = nextnode
    head=previous
    return head

# head = List()
#
# def reverse_list2_recursion(p):
#     if p.next == None:
#         head = p
#         return
#     reverse_list2_recursion(p.next)
#     q = p.next
#     q.next = p
#     p.next = None
    


     


        


if __name__ == "__main__":

    l0 = List()
    l1 = List()
    l2 = List()
    l3 = List()
    l4 = List()
    l5 = List()
    l6 = List()
    l7 = List()
    l8 = List()
    l9 = List()
    
    l0.val = 8
    l1.val = 5
    l2.val = 7
    l3.val = 9
    l4.val = 2
    l5.val = 1
    l6.val = 6
    l7.val = 4
    l8.val = 3
    l9.val = 0

    l0.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    l7.next = l8
    l8.next = l9
   
#print_list(l0)
#tail = reverse_list(l0)
#print_list(tail)

#tail = reverse_list2(l0)
#print_list(tail)

# reverse_list2_recursion(l0)
# print_list(head)

# print_list(l0)
# print("")
# head = bubble_sort(l0)
# print_list(head)

# print_list(l0)
# print("")
# head = selection_sort(l0)
# print_list(head)

print_list(l0)
print("")
head = insertion_sort(l0)
print_list(head)


