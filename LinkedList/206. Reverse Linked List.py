## Solution 1: Iterative Approach
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            nxt = curr.next ## temp variable

            curr.next = prev ## reverse the link
            prev = curr ## move pointer to the right
            curr = nxt ## move pointer to the right
        return prev
    

## Solution 2: Recursive Approach 
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## Recursive Approach
        if not head: ## if the head is empty
            return None

        newHead = head
        if head.next: ## if there's element afterwards
            newHead = self.reverseList(head.next) ## recursive call to the sub linked list
            head.next.next = head ## reverse the link
        head.next = None ## break the cycle, set the final node to point at None
        return newHead