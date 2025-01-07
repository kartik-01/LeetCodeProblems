#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.twoSum([2,3,4,5,6],11)
print(result)

## Try efficient solution