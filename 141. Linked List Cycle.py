# Solution
# Runtime: 56 ms, faster than 60.27% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.6 MB, less than 56.20% of Python3 online submissions for Linked List Cycle.

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        fast, slow = head, head
        
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
            
        return False