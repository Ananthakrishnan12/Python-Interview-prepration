class Solution:
    def Maximum_element(self,a):
        big=a[0]
        small=a[0]
        n=len(a)
        for i in range(1,n):
            if a[i]>big:
                big=a[i]
            if a[i]<small:
                small=a[i]
        return f"Maximum element in the list is:{big}"
    
a=[1,10,89,5,67,45]
soln=Solution()
res=soln.Maximum_element(a)
print(res)