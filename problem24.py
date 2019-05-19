class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        self.locked = False
        self.locked_desc = 0
        self.parent: None

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    self.left.parent = self
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    self.right.parent = self
                else:
                    self.right.insert(data)
        else:
            self.data = data

# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def is_lock(self):
        return self.lock

    def lockable_unlockable(self):
        if self.locked_desc > 0:
            return False

        node = self
        while node is not None:
            if node.locked:
                return False
            node = node.parent

        return True

    def lock(self):
        if not self.lockable_unlockable():
            return False

        self.locked = True

        node = self
        while node is not None:
            node.locked_desc += 1
            node = node.parent

        return True

    def unlock(self):
        if not self.lockable_unlockable():
            return False

        self.locked = False

        node = self
        while node is not None:
            node.locked_desc -= 1
            node = node.parent

        return True


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))