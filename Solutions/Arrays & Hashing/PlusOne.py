class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.plusOne([9,9])
print(result)

## Try efficient solution