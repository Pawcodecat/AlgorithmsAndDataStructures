class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, first = None, last = None):
        self.first = first
        self.last = last

    def is_empty(self):
        return self.first is None

    def make_from_array(self, array):
        if len(array) == 0:
            return
        self.first = Node(array[0])
        p = self.first
        self.last = p
        for i in range(1, len(array)):
            q = Node(array[i])
            p.next = q
            p = q
            self.last = p

    def add(self, val):
        node = Node(val)
        if self.is_empty():
            self.first = node
            self.last = node
            return
        self.last.next = node
        self.last = node

    def print_to_console(self):
        p = self.first
        while p is not None:
            print(p.val)
            p = p.next

    def has_one_element(self):
        return self.first == self.last

def merge_sorted_lists(List1, List2):
    if List1.is_empty():
        return List2

    result = LinkedList()
    p = Node()
    q = Node()
    r = Node()
    if List1.first.val <= List2.first.val:
        result.first = List1.first
        r = result.first
        result.last = r
        p = List1.first.next
        q = List2.first

    else:
        result.first = List2.first
        r = result.first
        result.last = r
        p = List2.first.next
        q = List1.first

    while p is not None and q is not None:
        while p is not None and q is not None and p.val <= q.val:
            r.next = p
            r = r.next
            result.last = r
            p = p.next
        while q is not None and p is not None and q.val <= p.val:
            r.next = q
            r = r.next
            result.last = r
            q = q.next

    while p is not None:
        r.next = p
        r = r.next
        result.last = r
        p = p.next

    while q is not None:
        r.next = q
        r = r.next
        result.last = r
        q = q.next
    return result

def split_list_into_halves(List):
    len = 0
    p = List.first
    while p is not None:
        len += 1
        p = p.next
    new_begin = List.first
    new_end = List.first
    for i in range(0, len//2):
        new_end = new_begin
        new_begin = new_begin.next
    new_begin = new_end.next
    new_end.next = None
    return (LinkedList(List.first, new_end), LinkedList(new_begin,List.last))

def merge_sort_on_linkedList(List):
    if List.is_empty() or List.has_one_element():
        return List
    first_half, second_half = split_list_into_halves(List)
    first_half_sorted = merge_sort_on_linkedList(first_half)
    second_half_sorted = merge_sort_on_linkedList(second_half)
    return merge_sorted_lists(first_half_sorted, second_half_sorted)


def concatenate_linked_list(array_of_linked_list):
    result = LinkedList()
    found_begining = False
    for i in array_of_linked_list:
        if not i.is_empty():
            i.last.next = None
    for i in array_of_linked_list:
        if not found_begining and not i.is_empty():
            found_begining = True
            result.first = i.first
            result.last = i.last
        elif not i.is_empty():
            result.last.next = i.first
            result.last = i.last
    return result

def quick_sort_linked_list(List):
    if List.is_empty() or List.has_one_element():
        return List
    smaller = LinkedList()
    equal = LinkedList()
    greater = LinkedList()
    p = List.first
    while p is not None:
        if p.val < List.last.val:
            smaller.add(p.val)
        elif p.val == List.last.val:
            equal.add(p.val)
        else:
            greater.add(p.val)
        p = p.next
    return concatenate_linked_list([quick_sort_linked_list(smaller), equal, quick_sort_linked_list(greater)])

class Node2:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

def partition_list(head, tail):
    pivot = head                    #choose pivot
    head = head.nextval
    pivot.next = None
    head_left = Node2()              #create guards
    head_right = Node2()
    tail_left, tail_right = head_left, head_right

    while(head):
        p, head = head, head.nextval
        if(p.dataval <= pivot):
            tail_left.nextval = p
            tail_left = p
        else:
            tail_right.next_val = p
            tail_right = p

    tail_left.nextval, tail_right.nextval = None, None
    head_left, head_right = head_left.next_val, head_right.nextval
    return head_left, tail_left, pivot, head_right, tail_right

def quick_sort_list(head, tail):
    if(head and not tail == head):
        head_left, tail_left, pivot, head_right, tail_right = partition_list(head,tail)
        head_left, tail_left = quick_sort_list(head_left, tail_left)
        head_right, tail_right = quick_sort_list(head_right, tail_right)
        if(head_left):
            tail_left.nextval = pivot
            head = head_left
        if head_right:
            pivot.nextval = head_right
            tail = tail_right
            tail.nextval = None
    return head, tail

if __name__ == '__main__':
    L = LinkedList()
    L.make_from_array([65,8756,1,2342,52,5636,76,35,1,85,6,8424,252])
    #L = merge_sort_on_linkedList(L)
    L = quick_sort_linked_list(L)
    L.print_to_console()






