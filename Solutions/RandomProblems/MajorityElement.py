# https://leetcode.com/problems/majority-element/description/
class Solution:
    def majorityElement(self, nums):
        countNum={}

        max_key = 0
        max_value = 0

        for num in nums:
            countNum[num] = 1 + countNum.get(num, 0)

        for key, value in countNum.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.majorityElement([2,2,1,1,1,2,2])
print(result)

## Try efficient solution