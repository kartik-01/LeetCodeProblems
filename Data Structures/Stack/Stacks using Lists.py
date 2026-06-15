class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def push(self, x):
        self.values.append(x)         # O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.values.pop()      # O(1)

    def peek(self):
        if self.is_empty():
            return None
        return self.values[-1]        # O(1)

    def size(self):
        return len(self.values)

my_stack = Stack()

try:
    print("pop on empty:", my_stack.pop())
except IndexError as e:
    print("pop on empty ->", e)

my_stack.pop()
print(my_stack.peek())
print(my_stack.size())

print(my_stack.push(1))
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.pop()
my_stack.pop()

my_stack.pop()
print(my_stack.values)
print(my_stack.peek())
