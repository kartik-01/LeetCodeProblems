#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def lcs(self, nums):
        charSet = set(nums)

        longest = 0

        for num in charSet:
            if num-1 not in charSet:
                length = 1
                while num+length in charSet:
                    length += 1
                longest = max(longest, length)
        
        return longest
        
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.lcs([100, 4, 200, 1, 3, 2])
print(result)

## Try efficient solution