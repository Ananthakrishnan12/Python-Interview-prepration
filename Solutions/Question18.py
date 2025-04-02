class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            new=curr.next
            curr.next=prev
            prev=curr
            curr=new
        return prev