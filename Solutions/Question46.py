class Solution:
    def doublechar(self,input):
        res=[]
        for char in input:
            res.append(char*2)
        return "".join(res)
    
    
input="Hi-There"          
soln=Solution()
result=soln.doublechar(input)
print(result)