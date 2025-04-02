class Solution:
    def non_repeated_str(self,s):
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in s:
            if d[i]==1:
                return i
        return " "

s="leetcode"
soln=Solution()
res=soln.non_repeated_str(s)
print(res)