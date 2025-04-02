# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_two_list(self,list1,list2):
        dummy=ListNode()
        current=dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
                
                
            current=current.next
        current.next=list1 or list2
        
        return dummy.next


list1=[1,2,4] 
list2=[1,3,4]

soln=Solution()
res=soln.merge_two_list(list1,list2)
print(res)