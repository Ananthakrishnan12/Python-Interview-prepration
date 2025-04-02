import re
class Solution:
    def countcode(self,input):
        s=re.compile(r"co.e")
        res=s.findall(input)
        return len(res)
    
    
input="cozexxcope"
soln=Solution()
result=soln.countcode(input)
print(result)
    
    