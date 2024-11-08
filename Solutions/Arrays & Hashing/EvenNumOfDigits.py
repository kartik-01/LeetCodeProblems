class Solution:
    def findNumbers(self, nums):
        def findEven(num):
            count = 0

            if num == 0:
                return 1
            
            while num > 0:
                count += 1
                num = num//10

            return count

        evenDigitCount = 0

        for num in nums:
            if findEven(num) % 2 == 0:
                evenDigitCount +=1
        return evenDigitCount
    
    # # by coverting it to string:
    #     even_digit_count = 0
    
    # # Iterate through each number in the list
    #     for num in nums:
    #         # Convert the number to a string and check if its length is even
    #         if len(str(num)) % 2 == 0:
    #             even_digit_count += 1
        
    #     return even_digit_count

    # one liner - return sum(1 for n in nums if len(str(n)) % 2 == 0)


# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.findNumbers([555,901,482,1771])
print(result)

## Try efficient solution