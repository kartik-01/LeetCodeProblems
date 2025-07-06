# https://leetcode.com/problems/encode-and-decode-strings/
class Solution:
    def encode(self, strs):
        encodedString = ''

        for s in strs:
            encodedString += str(len(s)) + '#' + s
        
        return encodedString
        pass

    def decode(self, encodedString):    # 6#params4#test
        res, i = [], 0

        while i < len(encodedString):
            j = i
            if encodedString[j] != '#':
                j=j+1
            length = int(encodedString[i:j])

            res.append(encodedString[j+1:j+1+length])
            i = j+1+length
        return res
        pass

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.encode(["params","test"])
resultTwo = sol.decode(result)
print(result)
print(resultTwo)

## Try efficient solution