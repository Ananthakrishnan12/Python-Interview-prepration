class Solution:
    def missing_numbers(self,nums):
        n=len(nums)
        s=(n*(n+1))//2
        total=0
        for i in nums:
            total=i+total
        return s-total

nums=[9,6,4,2,3,5,7,0,1]
soln=Solution()
res=soln.missing_numbers(nums)
print(res)