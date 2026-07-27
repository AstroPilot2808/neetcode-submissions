# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeTwoLists(self, head1, head2):
        answer = ListNode()
        curr = answer

        while head1 and head2:
            if head1.val <= head2.val:
                curr.val = head1.val
                curr.next = ListNode()
                curr = curr.next
                head1 = head1.next
            else:
                curr.val = head2.val
                curr.next = ListNode()
                curr = curr.next
                head2 = head2.next
        while head1:
            curr.val = head1.val
            head1 = head1.next
            if head1:
                curr.next = ListNode()
            curr = curr.next
        while head2:
            curr.val = head2.val
            head2 = head2.next
            if head2:
                curr.next = ListNode()
            curr = curr.next
        return answer