# Solution
# Runtime: 36 ms, faster than 93.97% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14.3 MB, less than 55.68% of Python3 online submissions for Remove Duplicates from Sorted List.

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(float('-inf'))
        dummy.next = head
        
        prev, curr = dummy, dummy.next
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return dummy.next