class Solution:
    def move_zeros(self,nums):
        a=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[a]
                nums[a]=temp
                a=a+1
        return nums
            

nums=[0, 1, 0, 3, 12]
soln=Solution()
res=soln.move_zeros(nums)
print(res)