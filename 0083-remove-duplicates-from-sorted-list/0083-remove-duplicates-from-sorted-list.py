# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        testset = set()
        
        dummy = ListNode(-1)
        
        dummy.next = head
        
        current_node = dummy
        
        while current_node.next is not None:
            if current_node.next.val in testset:
                current_node.next = current_node.next.next
            else:
                testset.add(current_node.next.val)
                current_node = current_node.next
        
        return dummy.next
        