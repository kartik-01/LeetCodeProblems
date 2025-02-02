# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def validPlindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.validPlindrome("kittik zz kittik")
print(result)

## Try efficient solution