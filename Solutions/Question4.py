import re

class Solution:
    def is_palindrome(self,strings):
        s="".join(re.sub("[^a-zA-Z]","",strings))
        g=s.lower()
        res=[]
        reslen=0
        for i in range(len(g)):
            l,r=i,i
            while l>=0 and r<len(g) and g[l]==g[r]: 
                if r-l+1>=len(g):
                    res=g[l:r+1]
                    reslen=r-l+1
                l=l-1
                r=r+1
            l,r=i,i+1
            while l>=0 and r<len(g) and g[l]==g[r]: 
                if r-l+1>=len(g):
                    res=g[l:r+1]
                    reslen=r-l+1
                l=l-1
                r=r+1
        return res==g
            
        
        
strings="A man, a plan, a canal, Panama"  
soln=Solution()
result=soln.is_palindrome(strings)
print(result)