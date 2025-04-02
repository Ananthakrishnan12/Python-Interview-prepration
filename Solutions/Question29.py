class Solution:
    def title_case(self,input):
        return " ".join(word.capitalize() for word in input.split())

input="python test"
soln=Solution()
res=soln.title_case(input)
print(res)