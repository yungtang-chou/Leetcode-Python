# Solution
# Runtime: 40 ms, faster than 52.20% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14 MB, less than 95.88% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
				## add in unfinished ListNode
        curr.next = l1 or l2
        return dummy.next