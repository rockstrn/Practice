# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        head1=ListNode(0)
        head1.next=head
        pre=head1
        while pre.next and pre.next.next:
            b=pre.next.next
            a=pre.next
            pre.next=b
            a.next=b.next
            b.next=a
            pre=pre.next.next
        return head1.next
