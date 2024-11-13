class Solution:
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start +(end - start) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                start = mid + 1

            elif nums[mid] > target:
                end = mid + 1
        
        return -1

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.binarySearch([3,9,12,15,22,35,45], 12)
print(result)

## Try efficient solution