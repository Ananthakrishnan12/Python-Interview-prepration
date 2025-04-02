class Solution:
    def swap_elements(self,input):
        size=len(input)
        temp=input[0]
        input[0]=input[size-1]
        input[size-1]=temp
        return input

input=[24,78,90,45,70]
soln=Solution()
res=soln.swap_elements(input)
print(res)