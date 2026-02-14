class Solution:
    def orderAgnosticbinarySearch(self, nums, target):
        l = 0
        r = len(nums) - 1

        isOrderAsc = True if nums[l] < nums[r] else False

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            
            elif isOrderAsc:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.orderAgnosticbinarySearch([45,30,21,20,15,5,3], 5)
print(result)

result2 = sol.orderAgnosticbinarySearch([3,5,15,20,21,30,45], 5)
print(result2)

## Try efficient solution