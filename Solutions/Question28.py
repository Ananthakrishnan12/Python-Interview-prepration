class Solution:
    def armstrong_number(self,nums):
        num_str=str(nums)
        num_digits=len(num_str)
        
        sum_of_powers=sum ( int(digits)** num_digits for digits in num_str)
        
        return sum_of_powers==nums


nums=1
soln=Solution()
res=soln.armstrong_number(nums)
print(res)