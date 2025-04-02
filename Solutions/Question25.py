class Solution:
    def second_largest(self,input):
        fst_maxval=input[0]
        for i in input:
            if i> fst_maxval:
                fst_maxval=i
        scnd_maxval=input[0]
        for i in input:
            if (i> scnd_maxval) and (i!=fst_maxval):
                scnd_maxval=i
        return scnd_maxval

input=[10, 20, 4, 45, 99]
soln=Solution()
res=soln.second_largest(input)
print(res)