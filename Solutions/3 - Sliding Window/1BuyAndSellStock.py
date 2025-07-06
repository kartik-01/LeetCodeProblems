# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                currP = prices[r] - prices[l]
                maxP = max(currP, maxP)
            else:
                l = r
            r+=1
        
        return maxP

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.maxProfit([7,1,5,3,6,4])
print(result)