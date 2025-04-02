class Solution:
    def two_sum(self,nums,target):
        hash_set={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hash_set:
                return(hash_set[diff],i)
            hash_set[n]=i
            
            
target=9
nums=[2,7,11,15]
soln=Solution()
res=soln.two_sum(nums,target)
print(res)