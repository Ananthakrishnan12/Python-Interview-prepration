import re

class Solution:
    def bobThere(self,input):
        s=re.compile(r"b.b")
        res=s.findall(input)
        if len(res)==0:
            return False
        else:
            return True
        
input="bac"       
soln=Solution()
result=soln.bobThere(input)
print(result)