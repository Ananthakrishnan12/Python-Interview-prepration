from collections import Counter

class Solution:
    def top_k_elements(self,nums,k):
        return [num for num,_ in Counter(nums).most_common(k)]
               
nums=[1,1,1,2,2,3]
k=2

soln=Solution()
res=soln.top_k_elements(nums,k)
print(res)