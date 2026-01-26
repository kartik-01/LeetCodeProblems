# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        min_len = float('inf')
        
        # 1. Pick every possible starting position
        for i in range(n):
            current_sum = 0
            
            # 2. Pick every ending position starting from i
            for j in range(i, n):
                current_sum += nums[j]
                
                # 3. Check if we hit the target
                if current_sum >= target:
                    current_len = j - i + 1
                    min_len = min(min_len, current_len)
                    
                    # Optimization: Since we want the MIN length, 
                    # there is no point adding more numbers to this specific start 'i'.
                    # We found the shortest valid one for this start.
                    break 
        
        return 0 if min_len == float('inf') else min_len

        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.minSubArrayLen(7, [2,3,1,2,4,3])
print(result)

## Try efficient solution