import ctypes

class Node(object):
    def __init__(self, data=None):
        self.npx = 0
        self.data = data

class XORList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.__nodes = []  # This is to prevent garbage collection

    def add_start(self,data=None):
        new_node = Node(data)

        if(self.head is None):
            self.head = self.tail = new_node
        else:
        #if list is not empty
            self.head.npx = id(new_node) ^ self.head.npx
            new_node.npx = id(self.head) # ^ 0
            self.head = new_node
        self.__nodes.append(new_node)

    def add_end(self,data=None):
        new_node = Node(data)

        if(self.head is None):
            self.head = self.tail = new_node
        else:
            self.tail.npx = id(new_node) ^ self.tail.npx
            new_node.npx = id(self.tail) # ^ 0
            self.tail = new_node

        self.__nodes.append(new_node)

    def printList(self):
        curr = self.head;
        prev_id = 0;

        while curr is not None:
            print(curr.data)
            # next = current.next ^ current.prev ^ prev
            next_id = curr.npx ^ prev_id
            if(next_id is not 0):
                prev_id = id(curr)
                curr =_get_obj(next_id)
            else:
                break

    def get(self,index):
        curr = self.head;
        prev_id = 0;

        for i in range(index):
            # next = current.next ^ current.prev ^ prev
            next_id = curr.npx ^ prev_id
            if (next_id is not 0):
                prev_id = id(curr)
                curr = _get_obj(next_id)
            else:
                print('Non ecziste')
                break

        print(curr.data)

def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value


list = XORList();
list.add_end(0)
list.add_end(1)
list.add_end(2)
list.add_end(3)
list.add_start(6)
list.printList();
list.get(3);