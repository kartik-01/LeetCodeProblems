class Solution:
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] < target:
                start = mid + 1
            
            else:
                end = mid - 1
        
        return nums[start%len(nums)]
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.binarySearch(['a','b','d','e','i','j'],'c')
print(result)

## Try efficient solution