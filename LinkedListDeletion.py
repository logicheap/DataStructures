class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        print("Printing linked list")
        while temp:
            print(temp.data)
            temp = temp.next

    def insertAtBeginning(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insertAfter(self, prev_node, data):
        if prev_node is None:
            print("Please provide a valid reference")
            return
        temp = Node(data)
        temp.next = prev_node.next
        prev_node.next = temp

    def append(self, data):
        temp = Node(data)
        last_node = self.head
        if self.head is None:
            self.head = temp
        while last_node.next :
            last_node = last_node.next
        last_node.next = temp

    def delete(self, data):
        prev_node = None
        cur_node = self.head
        if cur_node is not None:
            if cur_node.data == data:
                self.head = cur_node.next
                cur_node = None
                return
        while cur_node:
            if cur_node.data == data:
                prev_node.next = cur_node.next
                cur_node = None
                return
            prev_node = cur_node
            cur_node = cur_node.next

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

ll.insertAtBeginning(5)
ll.insertAfter(ll.head.next.next.next, 5)
ll.append(5)
ll.printList()
ll.delete(5)
ll.printList()
ll.delete(5)
ll.printList()
ll.delete(5)
ll.printList()
