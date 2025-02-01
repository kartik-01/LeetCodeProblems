class Solution:
    def orderAgnosticbinarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1

        isOrderAsc = True if nums[start] < nums[end] else False

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            elif isOrderAsc:
                if target  < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target  < nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.orderAgnosticbinarySearch([45,30,21,20,15,5,3], 5)
print(result)

## Try efficient solution