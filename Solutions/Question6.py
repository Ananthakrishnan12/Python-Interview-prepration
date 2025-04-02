class Solution:
    def count_vowels(self,input):
        vowels="aeiouAEIOU"
        count=0
        for i in input:
            if i in vowels:
                count+=1
        return count
    
input="Hello,world!"   
soln=Solution()
res=soln.count_vowels(input)
print(res)