class Solution:
    def reverse_integer(self,x):
        Max_value=2147483647
        Min_value=-2147483648
        
        sign=1 if x>=0 else -1
      
        x=x*sign
        
        reverse=int(str(x)[::-1])
        
        if (reverse<Min_value or reverse>Max_value):
            return 0
        
        return reverse*sign
    
    
x=123
soln=Solution()
res=soln.reverse_integer(x)
print(res)