# https://leetcode.com/problems/product-of-array-except-self/description/
def productExceptSelf(nums):
    # Time complexity O(n), Space Complexity O(n)
    n = len(nums)
    prefix, postfix, result = [1] * n, [1] * n, [1] * n

    prefix[0] = nums[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i]

    postfix[n-1] = nums[n-1]

    for i in range(n-2, -1, -1):
        postfix[i] = postfix[i+1] * nums[i]

    for i in range(n):
        if i == 0:
            result[i] = postfix[i+1]
        
        elif i == n-1:
            result[i] = prefix[i-1]
        
        else:
            result[i] = prefix[i-1] * postfix[i+1]

    return result
# Example usage:
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]

## Try efficient solution
# Time complexity O(n), Space Complexity O(1)

def productExceptSelf2(nums):
    res = [1] * len(nums)

    prefix=1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        
    return res

nums = [1,2,3,4]
print(productExceptSelf2(nums))  # Output: [24, 12, 8, 6]