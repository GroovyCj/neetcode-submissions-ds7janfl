# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next # Saving the true next node for later
            curr.next = prev # Instead of going  0 > 1 > 2 > 3 > None, this changes 0 > None
            prev = curr # Changes Prev to head, 0
            curr = temp # Moves node forward one, to continue loop
            
        return prev
        
        




        

        

        