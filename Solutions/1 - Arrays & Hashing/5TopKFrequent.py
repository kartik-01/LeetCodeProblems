# https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # Creates [ 0[], 1[], 2[], 3[], 4[], 5[], 6[]]

        for num in nums:                          # n : c
            count[num] = 1 + count.get(num, 0)    # {1: 3, 2: 2, 3: 1}
        
        for n, c in count.items():
            freq[c].append(n)                     # [ 0[], 1[3], 2[2], 3[1], 4[], 5[], 6[] ]
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.topKFrequent([1,1,1,2,2,3,4,4,4], 3)
print(result)

#Another Solution:
class AnotherSolution:
    def topKFrequent(self, nums, k):
        count={}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Sort elements by frequency in descending order
        sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        # Step 3: Return the top k elements
        return sorted_elements[:k]
    
# Create an instance of the class
sol = AnotherSolution()

# Call the method on the test cases
result = sol.topKFrequent([1,1,1,2,2,3,4,4,4], 3)
print("Effifient Solution", result)