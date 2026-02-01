from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        
        # 1. Setup the "Requirement" map
        countT = Counter(t)
        window = {} 
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            # --- EXPAND ---
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # If the current char count matches what we need in 't', we satisfy one condition
            if c in countT and window[c] == countT[c]:
                have += 1

            # --- SHRINK ---
            # While we have all the required characters...
            while have == need:
                # Update our result if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                # Pop from the left to try and make it smaller
                window[s[l]] -= 1
                
                # If we remove a required char and go below the needed count, 
                # we no longer "have" what we need.
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.minWindow('ADOBECODEBANC', 'ABC')
print(result)