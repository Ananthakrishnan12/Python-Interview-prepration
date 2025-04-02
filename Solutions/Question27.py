class Solution:
    def remove_duplicates(self,string):
        seen=set()
        result=[]
        for i in string:
            if i not in seen:
                seen.add(i)
                result.append(i)
        return "".join(result)

string="banana"
soln=Solution()
res=soln.remove_duplicates(string)
print(res)