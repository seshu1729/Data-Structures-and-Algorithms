# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        prev1 = dummy1
        prev2 = dummy2
        if head is None:
            return None
        current = head
        while current is not None:
            if current.val < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev2.next = None
        prev1.next = dummy2.next
        head = dummy1.next
        return head
        
