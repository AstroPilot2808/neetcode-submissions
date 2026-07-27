# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            if not nextNode:
                return curr
            curr = nextNode

        return None