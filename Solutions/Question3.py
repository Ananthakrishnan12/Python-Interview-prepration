class Solution:
    def reverse_array(self,arr):
        reverse=[]
        for i in arr:
            reverse.insert(0,i)
        return reverse
  
arr=[1,2,3,4,5]    
soln=Solution()
res=soln.reverse_array(arr)
print(res)