#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left+1, right+1]


# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.twoSum([1,3,4,5,6,9], 9)
print(result)

## Try efficient solution