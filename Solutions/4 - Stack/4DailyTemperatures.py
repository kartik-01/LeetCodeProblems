class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.dailyTemperatures([73,74,75,71,69,72,76,73])
print(result)