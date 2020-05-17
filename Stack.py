#Implementation of Stack using Python Lists

class Stack:

    def __init__(self):
        self._A = []

    def __len__(self):
        return len(self._A)

    def is_empty(self):
        return len(self._A)==0

    def push(self, item):
        self._A.append(item)

    def pop(self):
        if self.is_empty():
            return ("Stack is empty")
        return self._A.pop()

    def top(self):
        if self.is_empty():
            return ("Stack is empty")
        return self._A[-1]


S = Stack()
S.push(5)
print("Top is " + str(S.top()))
S.push(10)
print("Top is " + str(S.top()))
S.push(15)
print("Top is " + str(S.top()))
S.pop()
print("Top is " + str(S.top()))
S.pop()
print("Top is " + str(S.top()))
S.pop()
print("Top is " + str(S.top()))
S.pop()
print("Top is " + str(S.top()))

