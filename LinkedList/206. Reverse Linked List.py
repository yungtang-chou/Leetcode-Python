# Solution
# Runtime: 36 ms, faster than 68.33% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.6 MB, less than 45.50% of Python3 online submissions for Reverse Linked List.

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        dummy = ListNode(float('-inf'))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        
        return dummy.next
    