class Solution:
    def longest_substring(self,s):
        res_set=set()
        res=0
        l=0
        for i in range(len(s)):
            while s[i] in res_set:
                res_set.remove(s[i])
                l=l+1
            res_set.add(s[i])
            res=max(res,i-l+1)
            
        return res

s="abcabcbb"
soln=Solution()
res=soln.longest_substring(s)
print(res)