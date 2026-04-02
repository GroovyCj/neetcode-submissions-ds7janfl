# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1, and list2 aren't actually "lists" but a head node with a val and a next attribute
        # you must index the first head of each list, and check they are valid to loop through each list
        #after comparing the two list and entering the value in the dummy list, you must move the pointers for the list forward
        # depending on which node was added to the new list
        #then you must move the temp_node forward to the next node to compare its value to the next node item
        # if any value is left over, I.e. we get to the end of one list, we append any remaining values to the end of our new list

        temp_node = ListNode() # Make a dummy list to hold as the beginning of the new linked list
        tail = temp_node # a entry node to iterate forward through


        while list1 and list2: #Both list have to be valid for us to operate through
        
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next # move pointer to next node in list one
            else:
                # This line fires if list2 is greater than or equal to list1
                tail.next = list2
                list2 = list2.next
            tail = tail.next #move the tailer pointer to next in line



        if list1:
            tail.next =list1
        elif list2:
            tail.next = list2

        return temp_node.next # we need to return every value except the dummy node we added in the beginning 


