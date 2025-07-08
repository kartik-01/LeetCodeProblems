class Solution:
    # Bruteforce
    def characterReplacement(self, s, k):
        l = 0
        count = {}
        res = 0
        maxF = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            while (r-l + 1) - maxF > k:
                count[s[l]] -= 1
                l+=1
            res=max(res, (r-l+1))

        return res       
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.characterReplacement('ABABBA', 2)
print(result)

## Try efficient solution