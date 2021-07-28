# Solution
# Runtime: 60 ms, faster than 96.81% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 17.1 MB, less than 89.17% of Python3 online submissions for Remove Linked List Elements.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(float('-inf'))
        dummy.next = head
        
        pre, curr = dummy, dummy.next
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:                
                pre = curr
            curr = curr.next

        return dummy.next