class Solution:
    def reverse_string(self,strings):
        reverse=""
        for char in strings:
            reverse=char+reverse
        return reverse
    

strings="hello"    
soln=Solution()
res=soln.reverse_string(strings)
print(res)