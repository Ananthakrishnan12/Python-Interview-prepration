class Solution:
    def reverse_words(self,input):
        words=input.split()
        ans=""
        for char in words:
            ans=char+" "+ans
        return ans.strip()

            
input="a good   example"
soln=Solution()
res=soln.reverse_words(input)
print(res)