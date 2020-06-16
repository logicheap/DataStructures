#This import is of the class Queue that we created in Queue chapter(https://github.com/logicheap/DataStructures/blob/master/Queue.py)
from queue import Queue

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
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

    def levelorder_traversal(self, root):
        Q = Queue()
        if root != None:
            Q.enqueue(root)

        while(not Q.is_empty()):
            temp = Q.dequeue()
            print(temp.data)
            if temp.left is not None:
                Q.enqueue(temp.left)
            if temp.right is not None:
                Q.enqueue(temp.right)

    def insert(self, value):
        Q = Queue()
        if self.root != None:
            Q.enqueue(self.root)
        else:
            self.root = Node(value)

        while(len(Q) > 0):
            temp = Q.dequeue()

            if temp.left is not None:
                Q.enqueue(temp.left)
            else:
                temp.left = Node(value)
                break

            if temp.right is not None:
                Q.enqueue(temp.right)
            else:
                temp.right = Node(value)
                break

    def delete_last_node(self, delete_node):
        Q = Queue()
        if self.root != None:
            if(self.root == delete_node):
                self.root = None
                return
            Q.enqueue(self.root)

        while (not Q.is_empty()):
            temp = Q.dequeue()
            if temp.left is not None:
                if temp.left == delete_node:
                    temp.left = None
                    break
                else:
                    Q.enqueue(temp.left)
            if temp.right is not None:
                if temp.right == delete_node:
                    temp.right = None
                    break
                else:
                    Q.enqueue(temp.right)


    def delete(self, value):
        Q = Queue()
        if self.root != None:
            Q.enqueue(self.root)
        while (not Q.is_empty()):
            temp = Q.dequeue()
            if temp.data == value:
                key_node = temp
            if temp.left is not None:
                Q.enqueue(temp.left)
            if temp.right is not None:
                Q.enqueue(temp.right)

        if key_node:
            key_node.data = temp.data
            self.delete_last_node(temp)


T = BinaryTree()

T.root = Node(10)
T.root.left = Node(20)
T.root.right = Node(30)
T.root.left.left = Node(40)
T.root.left.right = Node(50)
T.root.right.right = Node(60)
print("Inorder traversal of tree")
T.inorder_traversal(T.root)
print("Preorder traversal of tree")
T.preorder_traversal(T.root)
print("Postorder traversal of tree")
T.postorder_traversal(T.root)
print("Levelorder traversal of tree")
T.levelorder_traversal(T.root)
value = input("Provide a value for the insertion")
T.insert(value)
print("Levelorder traversal of tree after insertion")
T.levelorder_traversal(T.root)
T.levelorder_traversal(T.root)
print("deleting")
T.delete(10)
T.levelorder_traversal(T.root)

T2 = BinaryTree()
T2.root = Node(10)
T2.levelorder_traversal(T2.root)
print("deleting")
T2.delete(10)
T2.levelorder_traversal(T2.root)





