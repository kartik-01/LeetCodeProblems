from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())

sol = Solution()

# Call the method on the test cases
result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)


takeinput = float(input("provide your input:"))
print(takeinput)