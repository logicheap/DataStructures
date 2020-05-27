
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

T = BinaryTree()

T.root = Node(10)
T.root.left = Node(20)
T.root.right = Node(30)
T.root.left.left = Node(40)
T.root.left.right = Node(50)
T.root.right.right = Node(60)
