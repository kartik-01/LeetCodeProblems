#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def lcs(self, nums):
        numSet = set(nums)
        print(numSet)
        longest = 0
        
        for n in nums:
            if (n-1) not in nums:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
        
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.lcs([100, 4, 200, 1, 3, 2])
print(result)

## Try efficient solution