class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                # If stack is not empty and top of stack is the matching opener
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(c)
        
        # If stack is empty, return True; else False
        return True if not stack else False
# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.isValid("()[]{}")
print(result)

## Try efficient solution