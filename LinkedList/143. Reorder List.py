# Solution
# Runtime: 92 ms, faster than 72.55% of Python3 online submissions for Reorder List.
# Memory Usage: 23.3 MB, less than 49.00% of Python3 online submissions for Reorder List.


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next
        
        while curr:
            q.append(curr)
            curr = curr.next
        
        curr = dummy
        even = False
        while q:
            node = q.pop() if even else q.popleft()
            node.next = None
            curr.next = node
            curr = curr.next
            even ^= True
        return dummy.next

# Solution 2
# Runtime: 88 ms, faster than 86.79% of Python3 online submissions for Reorder List.
# Memory Usage: 23.2 MB, less than 79.49% of Python3 online submissions for Reorder List.

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return []
        
        dummy = ListNode(0)
        dummy.next = head
        # find the middle node -> slow and fast pointer
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half -> prev, curr, nxt
        prev, curr = None, slow.next
        while curr:
            nxt = curr.next
            curr.next, prev, curr = prev, curr, nxt
        
        # set slow.next = None to remove cycle --> no ongoing nodes
        slow.next = None
        
        # merge the first half and the second half
        head1, head2 = head, prev
        
        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp
        
        return dummy.next
            