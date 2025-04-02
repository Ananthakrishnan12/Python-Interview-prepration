class Solution:
    def reverse_string(self,string):
        stack=[]
        for i in string:
            stack.append(i)
        i=0
        while len(stack)>0:
            a=stack.pop()
            string[i]=a
            i=i+1
        return string
        
string=["h","e","l","l","o"]       
soln=Solution()
res=soln.reverse_string(string)
print(res)