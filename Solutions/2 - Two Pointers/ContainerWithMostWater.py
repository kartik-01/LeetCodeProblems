# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1

        res = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return res

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(result)

## Try efficient solution