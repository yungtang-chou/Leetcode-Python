# Solution
# Runtime: 164 ms, faster than 63.60% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 29.1 MB, less than 99.08% of Python3 online submissions for Intersection of Two Linked Lists.


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA, nodeB = headA, headB
        while nodeA is not nodeB:
            nodeA = headB if not nodeA else nodeA.next
            nodeB = headA if not nodeB else nodeB.next
        return nodeA