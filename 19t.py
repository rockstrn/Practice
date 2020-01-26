# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def ss(nod,n):
            for i in range(n):
                nod=nod.next
            if nod.next==None:
                return bool(1)
            else:
                return bool(0)
        head1=ListNode(0)
        head1.next=head
        head2=head1
        while head1:
            if ss(head1,n):
                head1.next=head1.next.next
                return head2.next
            else:
                head1=head1.next
