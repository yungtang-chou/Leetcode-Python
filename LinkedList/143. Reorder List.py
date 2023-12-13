class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        ## 0. find the middle poinrt to split linked list into 2
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        ## 1. reverse the second portion of the linked list, LC 206
        second = slow.next ## get the second half the linkedlist
        prev = slow.next = None

        while second:
            temp = second.next

            second.next = prev
            prev = second
            second = temp


        ## 2. merge the two linked list, LC 21
        first, second = head, prev

        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2