class MinStack:

    def __init__(self):
        self.values = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.values.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.values.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

def run_leetcode_example():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # return -3
    minStack.pop()
    print(minStack.top())    # return 0
    print(minStack.getMin()) # return -2

run_leetcode_example()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()