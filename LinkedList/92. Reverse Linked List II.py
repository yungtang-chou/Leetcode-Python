# Solution
# Runtime: 32 ms, faster than 61.85% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14.3 MB, less than 90.10% of Python3 online submissions for Reverse Linked List II.


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(float('-inf'))
        dummy.next = head
        
        prev, curr = dummy, dummy.next
        
        for i in range(left - 1):
            prev = prev.next

        curr = prev.next
        for i in range(right - left):
            nxt = curr.next
            prev.next, curr.next, nxt.next = nxt, nxt.next, prev.next
           # prev.next    curr.next         curr.next.next
           # curr.next    curr.next.next    prev.next

        return dummy.next
    
    