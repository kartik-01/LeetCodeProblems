# https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def ValidAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            print(c)
            print(countS[c], end='')
            print(countT.get(c, 0))
            if countS[c] != countT.get(c, 0):
                return False

        return True

# Create an instance of the class
sol = Solution()

# Call the method on the instance
result = sol.ValidAnagram("anagram","gramana")
print(result)

## Try efficient solution