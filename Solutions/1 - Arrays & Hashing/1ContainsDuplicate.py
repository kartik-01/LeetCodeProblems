# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
# Create an instance of the class
sol = Solution()

# Call the method on the instance
result = sol.containsDuplicate([1,3,4,1,5])
print(result)

## Try efficient solution