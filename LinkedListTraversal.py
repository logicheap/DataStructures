

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

ll = LinkedList()

firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)
fourthNode = Node(40)

ll.head = firstNode
firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode

ll.printList()



