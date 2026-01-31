#https://leetcode.com/problems/two-sum/
class Solution:
## BruteForce solution - O(n2)
    def twoSum(self, nums,target):
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                
## Optimized solution - O(n)
    def twoSumOptimized(self, nums,target):
        prevMap = {}
        for i, a in enumerate(nums):
            diff = target - a
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[a] = i
        return

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.twoSum([2,3,4,5,6],11)
print(result)

result = sol.twoSumOptimized([2,3,4,5,6],11)
print(result)


