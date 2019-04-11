class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.isUnival = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val),
        if self.right:
            self.right.PrintTree()

    def insert(self, data):
        # Compare the new value with the parent node
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    # receive a root of a tree
    def unival(self, count):
        if (self.right is None) and (self.left is None):
            self.isUnival = self.val
            return count + 1
        count = self.right.unival(count) + self.left.unival(count)
        if self.val == self.right.isUnival == self.left.isUnival:
            self.isUnival = self.val
            count += 1
        return count


node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
count = 0
count = node.unival(count)
print(count)



