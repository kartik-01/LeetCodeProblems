class Solution:
    def maximumWealth(self, accounts):
        def sumOfCustomerWealth(customer):
            wealth = 0
            for amount in customer:
                wealth = wealth + amount
            return wealth
        
        richestWealth = 0

        for customer in accounts:
            customerWealth = sumOfCustomerWealth(customer)

            if customerWealth > richestWealth:
                richestWealth = customerWealth

        return richestWealth


# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.maximumWealth([[1,2,3],[3,2,1]])
print(result)

## Try efficient solution