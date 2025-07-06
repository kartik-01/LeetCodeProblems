# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.checkAlpha(s[l]):
                l+=1
            while r > l and not self.checkAlpha(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        
        return True
    
    def checkAlpha(self, s):
        return (ord('a') <= ord(s) <= ord('z') or
                ord('A') <= ord(s) <= ord('Z') or
                ord('0') <= ord(s) <= ord('9'))


# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.validPlindrome("kartik izi kitrak")
print(result)

## Try efficient solution