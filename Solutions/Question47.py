class Solution:
    def transforming(self,input):
        res=[]
        vowels="aeiouAEIOU"
        for char in input:
            if char in vowels:
                res.append(char*2)
            elif char not in vowels:
                res.append(char*3)
        return "".join(res)
    
input="AI-Model"   
soln=Solution()
result=soln.transforming(input)
print(result)
                