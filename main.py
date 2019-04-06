class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize_print(root):
    if root != None:
        print('(',end='')
        print(root.val,end='')
        serialize(root.right)
        serialize(root.left)
        print(')',end='')
    else:
        print('()',end='')

def serialize(root):
    result=""
    if root != None:
        result+=root.val
        result+=' '
        result+=serialize(root.right)
        result+=serialize(root.left)
    else:
        result+='# '
    return result

def deserialize(serie):
    def aux_deserialize():
        aux = next(aux_iter)
        if (aux == '#' ):
            return None
        else:
            node = Node(aux)
            node.right = aux_deserialize()
            node.left = aux_deserialize()
            return node

    aux_iter = iter(serie.split())  # create a object wich can be itered
    return aux_deserialize()

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'