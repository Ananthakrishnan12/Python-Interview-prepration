class Solution:
    def is_palindrome(self,input):
        s=str(input)
        res=[]
        reslen=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>=reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l=l-1
                r=r+1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>=reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l=l-1
                r=r+1
                
        return res==s
            
input=12321
soln=Solution()
result=soln.is_palindrome(input)
print(result)