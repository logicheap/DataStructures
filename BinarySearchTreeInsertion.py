class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, root):
        if root==None:
            return
        else:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root == None:
            return
        else:
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root == None:
            return
        else:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data)

    def search(self, root, value):
        if root:
            if root.data == value:
                return root
            elif root.data > value:
                return self.search(root.left, value)
            else:
                return self.search(root.right, value)

    def insert(self, root, value):
        if root is None:
            self.root = Node(value)
        else:
            if root.data < value :
                if root.right is None:
                    root.right = Node(value)
                else:
                    self.insert(root.right, value)
            else:
                if root.left is None:
                    root.left = Node(value)
                else:
                    self.insert(root.left, value)





T = BinarySearchTree()

T.root = Node(50)
T.root.left = Node(20)
T.root.right = Node(70)
T.root.left.left = Node(15)
T.root.left.right = Node(35)
T.root.right.right = Node(90)

print("Inorder traversal of tree")
T.inorder_traversal(T.root)

#calling search method of BST to find value 90
search_result = T.search(T.root, 90)


if search_result:
    print("Searched value " + str(search_result.data) + " found")
else:
    print("value not found")

T.insert(T.root, 100)
print("Inorder traversal of tree after insertion")
T.inorder_traversal(T.root)
