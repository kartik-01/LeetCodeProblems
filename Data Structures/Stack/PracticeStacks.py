class Stack:
    def __init__(self):
        self.values = []

    def isEmpty(self):
        return len(self.values) == 0
        pass

    def push(self, val):
        self.values.append(val)

    def pop(self):
        if not self.isEmpty():
            self.values.pop()
        else:
            raise IndexError("cannot pop from an empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.values[-1]
        pass

    def size(self):
        return len(self.values)
        pass

    def get(self):
        if not self.isEmpty():
            return stack.values
        return ("Stack is empty")

stack = Stack()

print(stack.size())
print(stack.isEmpty())
print(stack.peek())
print(stack.get())

(stack.push(10))
(stack.push(20))
(stack.push(30))
(stack.push(40))

print(stack.peek())
print(stack.get())
stack.pop()

print(stack.get())