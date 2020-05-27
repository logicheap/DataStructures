#Implementation of Queue using Python Lists

class Queue:

    def __init__(self):
        self._A = []

    def __len__(self):
        return len(self._A)

    def is_empty(self):
        return len(self._A)==0

    def enqueue(self, item):
        self._A.append(item)

    def dequeue(self):
        if self.is_empty():
            return ("Queue is empty")
        return self._A.pop(0)

    def first(self):
        if self.is_empty():
            return ("Queue is empty")
        return self._A[0]


Q = Queue()
Q.enqueue(10)
print("First element is " + str(Q.first()))
print("Length of Queue is " +  str(len(Q)))
Q.enqueue(20)
print("First element is " + str(Q.first()))
print("Length of Queue is " +  str(len(Q)))
Q.enqueue(30)
print("First element is " + str(Q.first()))
print("Length of Queue is " +  str(len(Q)))
removed_element = Q.dequeue()
print("Dequeued " + str(removed_element))
print("First element is " + str(Q.first()))
print("Length of Queue is " +  str(len(Q)))


