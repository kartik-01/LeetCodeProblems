class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# Create an instance of the class
sol = Solution()

# Call the method on the instance
result = sol.containsDuplicate([1,3,4,5])
print(result)

## Try efficient solution