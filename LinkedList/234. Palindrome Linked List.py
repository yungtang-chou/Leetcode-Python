# Solution
# Runtime: 812 ms, faster than 63.08% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 46.9 MB, less than 57.48% of Python3 online submissions for Palindrome Linked List.

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = ListNode(0)
        fast = slow = head
        stack = []
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        
        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()
            if slow.val != top:
                return False
            slow = slow.next
        return True
    
    
# Solution 2
# Runtime: 800 ms, faster than 68.91% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 46.9 MB, less than 57.48% of Python3 online submissions for Palindrome Linked List.

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack == stack[::-1]