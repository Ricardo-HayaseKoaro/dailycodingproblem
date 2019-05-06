class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


def list_intersect_brute_force(ls1, ls2):
    curr_node1 = ls1.headval  # root of list 1
    curr_node2 = ls2.headval  # root of list 2
    while curr_node2 is not None:
        while curr_node1 is not None:
            if curr_node1 == curr_node2:
                print(curr_node1.dataval)
                return True
            curr_node1 = curr_node1.nextval
        curr_node2 = curr_node2.nextval


def list_intersect_without_mem_opt(ls1, ls2):
    curr_node1 = ls1.headval  # root of list 1
    curr_node2 = ls2.headval  # root of list 2
    aux = set()
    while curr_node1 is not None:
        aux.add(curr_node1)
        curr_node1 = curr_node1.nextval

    while curr_node2 is not None:
        if curr_node2 in aux:
            print(curr_node2.dataval)
            return True
        curr_node2 = curr_node2.nextval


def length(list):
    i = 0
    curr_node = list.headval
    while curr_node is not None:
        curr_node = curr_node.nextval
        i += 1
    return i


def list_intersect(ls1, ls2):
    n1 = length(ls1)
    n2 = length(ls2)
    curr_node1 = ls1.headval
    curr_node2 = ls2.headval

    if n2 > n1:
        for i in range(n2 - n1):
            curr_node2 = curr_node2.nextval
    else:
        for i in range(n1 - n2):
            curr_node1 = curr_node1.nextval

    while curr_node1 is not None:
        if curr_node2 == curr_node1:
            print(curr_node2.dataval)
            return True
        curr_node1 = curr_node1.nextval
        curr_node2 = curr_node2.nextval

    return False


list = SLinkedList()
list2 = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.AtEnd("Thu")
list2.headval = e2
list.listprint()
print()
list2.listprint()
print()
list_intersect(list, list2)
list_intersect_brute_force(list, list2)
list_intersect_without_mem_opt(list, list2)