# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(s1: str, s2: str) -> bool:
        n1,n2 = len(s1), len(s2)

        if n1 > n2: return False                    # Base edge case

        s1_counts, s2_counts = [0] * 26, [0] * 26

        for i in range(n1):                         # Calculate initial window of len s1
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
        
        if s1_counts == s2_counts: return True

        for i in range(n1,n2):                      # Calculate remaining window of s2 by sliding
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1

            if s1_counts == s2_counts: return True  # keep checking if window matches after every +1 slide of window
        
        return False

    # Example usage:
    s1 = "abc"
    s2 = "eidbcaooo"
    print(checkInclusion(s1, s2))  # Output: True
