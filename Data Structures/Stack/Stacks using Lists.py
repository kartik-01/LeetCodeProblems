class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def push(self, x):
        self.values.append(x)

    def pop(self):
        if not self.is_empty():
            self.values.pop()
        return IndexError("Cannot pop from an empty stack.")
    
    def peek(self):
        if not self.is_empty():
            return self.values[-1]
        return None

    def size(self):
        return len(self.values)

my_stack = Stack()

print(my_stack.pop())
print(my_stack.peek())
print(my_stack.size())

print(my_stack.push(1))
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)

my_stack.pop()
print(my_stack.values)
print(my_stack.peek())