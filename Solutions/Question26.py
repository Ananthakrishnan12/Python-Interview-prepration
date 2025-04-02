class Solution:
    def find_pairs(self,nums,target):
        seen=set()
        pair=[]
        for i in nums:
            compilement=target-i
            if compilement in seen:
                pair.append((compilement,i))
            seen.add(i)
        return pair


nums=[1, 2, 3, 4, 5, 6, 7]
target=8
soln=Solution()
res=soln.find_pairs(nums,target)
print(res)