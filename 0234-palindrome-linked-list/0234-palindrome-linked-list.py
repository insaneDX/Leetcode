# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Step 1: Find the middle node using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        curr = slow
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Compare the first half and the reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        
        return True

# Problem statement: Check if a singly linked list is a palindrome.
# Example: [1, 2, 2, 1] is a palindrome.
# Steps:
# 1. Find the middle node.
# 2. Reverse the second half of the list.
# 3. Compare both halves for equality.

# Time Complexity: O(n)
# Finding the middle: The while fast and fast.next loop traverses half the list -> O(n/2)
# Reversing the second half: Another traversal of half the list -> O(n/2)
# Comparing both halves: Full traversal of the second half again -> O(n/2)
# O(n) where n is the number of nodes in the linked list.

# Space Complexity: O(1)