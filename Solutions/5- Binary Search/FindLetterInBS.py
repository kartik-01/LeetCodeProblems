#https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def findSmallestGreaterLetter(self, letters, target):
        start = 0
        end = len(letters) - 1

        while start <= end:
            mid = start + ( end - start) // 2

            if target < letters[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return letters[start%len(letters)]
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.findSmallestGreaterLetter(['a', 'b', 'c', 'g', 'i','l'], 'b')
print(result)

## Try efficient solution