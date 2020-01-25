# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        b=ListNode(0)
        a=b
        jin=0
        while (l1 or l2):
            x=l1.val if l1!=None else 0
            y=l2.val if l2!=None else 0
            s=jin+x+y
            a.next=ListNode(s%10)
            jin=s//10
            a=a.next
            if(l1!=None):
                l1=l1.next
            if(l2!=None):
                l2=l2.next
        if(jin==1):
            a.next=ListNode(1)
        return b.next
