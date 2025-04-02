class Solution:
    def common_prefix(self,strings):
        if not strings:
            return " "
        
        shortest=min(strings,key=len)
        
        for i in range(len(shortest)):
            for words in strings:
                if words[i]!=shortest[i]:
                    return shortest[:i]
            
        return shortest


strings=["flower","flow","flight"]
soln=Solution()
res=soln.common_prefix(strings)
print(res)