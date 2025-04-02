class Solution:
    def count_frequency_words(self,input):
        words=input.split()
        d={}
        for i in words:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        return d

input="apple banana apple orange banana apple"
soln=Solution()
res=soln.count_frequency_words(input)
print(res)