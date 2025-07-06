#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] + nums[r] > target:
                r-=1
            elif nums[l] + nums[r] < target:
                l+=1
            else:
                return [l+1, r+1]


# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.twoSum([1,3,4,5,6,9], 9)
print(result)

## Try efficient solution