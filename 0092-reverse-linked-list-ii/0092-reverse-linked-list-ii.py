class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # prev will point to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # reverse by repeatedly taking the node after 'curr' and moving it to the front
        curr = prev.next  # this is the 'left' node
        for _ in range(right - left):
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode

        return dummy.next