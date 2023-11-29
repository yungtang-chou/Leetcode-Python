# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ## start of the linked list
        dummy = ListNode()
        tail = dummy
        
        ## if both of them are non-empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next ## pointer move to the next node

        if list1: ## if there's still remaining in list1, append the entire listnodes
            tail.next = list1
        
        if list2:
            tail.next = list2

        return dummy.next ## return everything after the dummy header