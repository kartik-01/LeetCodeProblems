class Solution:
    def findFloor(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        
        return end
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.findFloor([3,6,8,11,14,17,25,30], 7)
print(result)

## Try efficient solution