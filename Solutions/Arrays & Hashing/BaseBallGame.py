#https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations):
        stack = []

        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])

            elif op == 'C':
                stack.pop()

            elif op == 'D':
                stack.append(2 * stack[-1])

            else:
                stack.append(int(op))
        
        return sum(stack)

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.calPoints(["5","2","C","D","+"])
print(result)
