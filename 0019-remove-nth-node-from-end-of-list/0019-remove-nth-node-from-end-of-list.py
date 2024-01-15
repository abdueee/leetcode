# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       #declare dummy
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #loop for assigning right position
        while n>0 and right:
            right = right.next
            n-=1
        
        #looping left and right
        while right:
            left = left.next
            right = right.next
        
        #severing node
        left.next = left.next.next
        
        return dummy.next