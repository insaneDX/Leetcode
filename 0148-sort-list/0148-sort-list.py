# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if empty and signle list
        if not head or not head.next:
            return head
        
        # function to split the link list in two halves
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid
        
        # function to mergesort
        def merge(left, right): 
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val <= right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left if left else right
            return dummy.next

        def mergeSort(head):
            if not head or not head.next:
                return head
            left, right = split(head) # find left and right portion
            left = mergeSort(left)    # recursively find left and right portion of left subarray
            right = mergeSort(right)  # recursively find left and right portion of right subarray
            merged =  merge(left, right) # merge left and right portion
            return merged
        
        return mergeSort(head)

# def print_list(head):
#     while head:
#         print(head.val, end=" -> ")
#         head = head.next
#     print("None")

# nodes = [ListNode(38), ListNode(27), ListNode(43), ListNode(3), ListNode(9), ListNode(82), ListNode(10)]
# for i in range(len(nodes) -1):
#     nodes[i].next = nodes[i+1]

# head = nodes[0]
# solver = Solution()
# sorted_head = solver.sortList(head)
# print_list(sorted_head)