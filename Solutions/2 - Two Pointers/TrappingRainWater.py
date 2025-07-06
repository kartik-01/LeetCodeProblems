# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        res = 0

        while l < r:
            if maxLeft < maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
            
        return res
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(result)

## Try efficient solution