class Solution:
    def run_length_encoding(self,input):
        if not input:
            return " "
        
        result=[]
        count=1
        
        for i in range(1,len(input)):
            if input[i]==input[i-1]:
                count+=1
                
            else:
                result.append(input[i-1]+(str(count) if count>1 else ""))
                count=1
        result.append(input[-1]+(str(count) if count>1 else  ""))
        return "".join(result)
    
    
    
input="aaabbc"
soln=Solution()
res=soln.run_length_encoding(input)
print(res)