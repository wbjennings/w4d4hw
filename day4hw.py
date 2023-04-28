class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def bst_decorator(func):
    def wrapper(lst):
        root = None
        for val in lst:
            root = insert(root, val)
        return func(root)
        
    return wrapper

def find_max(node):
    if node.right:
        return find_max(node.right)
    return node.val
    
lst = [2,1,3,4,5]
print(find_max(lst))
    


