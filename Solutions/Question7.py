class Solution:
    def factorial(self,n):
        if n==0:
            return 1
        else:
            return n * self.factorial (n - 1)
        
number=int(input("Enter the number of your choice:"))
soln=Solution()
res=soln.factorial(number)
print(res)