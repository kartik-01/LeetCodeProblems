# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            right += 1
        
        return maxP
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.maxProfit([7,1,5,3,6,4])
print(result)