# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the result list
        dummy = ListNode(0)
        curr = dummy

        # Initialize pointers for list1 and list2
        curr_i = list1
        curr_j = list2

        # Merge smaller elements first
        while curr_i and curr_j:
            if curr_i.val < curr_j.val:
                curr.next = curr_i
                curr_i = curr_i.next
            else:
                curr.next = curr_j
                curr_j = curr_j.next
            curr = curr.next

        #If there are remaining nodes in either list, append them to the result
        if curr_i:
            curr.next = curr_i
        elif curr_j:
            curr.next = curr_j

        return dummy.next