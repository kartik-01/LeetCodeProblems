# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
class Solution:
    def singleElement(self, nums):
        min_key=0
        min_value=float('inf')

        count={}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, value in count.items():
            if value < min_value:
                min_value = value
                min_key = key
        return min_key

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.singleElement([1])
print(result)

## Try efficient solution