class Solution:
    def LCP(self, strs):
        res = []
        
        for i in range(len(strs[0])):
            print(i,'len ', len(strs[0]))
            for s in strs:
                print('strs ',s)
                print('s[i]', s[i], 'strs[0][i]', strs[0][i])
                if i == len(s) or s[i] != strs[0][i]:
                    print('inner !',res)
                    return "".join(res) 
            res.append(strs[0][i]) 
            print('outer !!',res)
        return "".join(res)

            

# Create an instance of the class
sol = Solution()
s = ["donkey",'doni','dog']
# Call the method on the test cases
result = sol.LCP(s)
print(result)

## Try efficient solution