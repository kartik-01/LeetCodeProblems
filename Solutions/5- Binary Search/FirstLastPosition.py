#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums, target):
        def search(nums, target, isFirstIndex):
            ans = - 1
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = start + (end - start) // 2

                if target < nums[mid]:
                    end = mid - 1
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    # potential ans has been found
                    ans = mid
                    if isFirstIndex:
                        end = mid - 1
                    else:
                        start = mid + 1
            return ans
        
        ans = [-1,-1]
        
        start = search(nums, target, isFirstIndex=True)
        end = search(nums, target, isFirstIndex=False)

        ans[0] = start
        ans[1] = end

        return ans
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.searchRange([5,7,7,8,8,10], 8)
print(result)

## Try efficient solution