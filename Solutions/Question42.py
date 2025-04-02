list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

class Solution:
    def common_elements(self,list1,list2):
        return [ i for i in list1 if i in list2]
            
soln=Solution()
res=soln.common_elements(list1,list2)
print(res)
                