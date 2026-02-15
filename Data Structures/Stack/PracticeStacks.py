class Stack:
    def __init__(self):
        pass
    def is_empty(self):
        pass
    def push(self, x):
        pass
    def pop(self):
        pass
    def peek(self):
        pass
    def size(self):
        pass
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