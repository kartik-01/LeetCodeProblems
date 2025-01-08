class Solution:
    def __init__(self, initial_stack=None):
        self.stack = initial_stack if initial_stack is not None else []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    
sol = Solution([3,4,5,6])

sol.push(7)

print(sol.peek())

sol.pop()

print(sol.peek())

mylist=[12,12,32,42]

print(mylist)

print(mylist[-1])