class Solution:
    def getFact(self, n):
        if n < 0:
            return -1
        if n < 2:
            return 1
        else:
            return n * self.getFact(n-1)
        
    def EvenNums(self, n):
        print(n)
        if n%2 != 0:
            print('Please enter even input')
        elif n == 2:
            return n
        else:
            return self.EvenNums(n-2)
        
    def Fibo(self, n):
        if n <= 1:
            return n
        return  self.Fibo(n-1) + self.Fibo(n-2)
        
sol = Solution()

print(sol.Fibo(8))
