class Solution:
    def encode(self, strs):
        # encodedString=""
        # for s in strs:
        #     encodedString += str(len(s)) +'#' +s
        # return encodedString
    
        return ''.join([str(len(s)) + "#" + s for s in strs])

    def decode(self, encoded_str):
        decoded_strings, i = [], 0
        
        while i < len(encoded_str):
            # Find the position of the next '#'
            j = encoded_str.find('#', i)

            print("decodedJ",j)
            
            # Extract the length of the next string
            length = int(encoded_str[i:j])

            print("length", length)
            
            # Extract the actual string using the length
            decoded_strings.append(encoded_str[j+1:j+1+length])
            
            # Move to the next part of the encoded string
            i = j + 1 + length
        
        return decoded_strings

# Create an instance of the class
sol = Solution()

# Call the method on the test cases
result = sol.encode(["params","test"])
resultTwo = sol.decode(result)
print(result)
print(resultTwo)

## Try efficient solution