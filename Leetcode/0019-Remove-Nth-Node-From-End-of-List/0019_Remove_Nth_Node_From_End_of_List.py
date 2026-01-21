# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        if fast.next is None:
            head = None
            return head
        elif fast.next.next is None:
            if n == 1:
                head.next = None
                return head
            elif n==2:
                head = head.next
                return head
        else:
            for _ in range(n):
                fast = fast.next
            if fast is None:
                head = head.next
                return head
            else:
                while fast is not None and fast.next is not None:
                    slow = slow.next
                    fast = fast.next
                slow.next = slow.next.next
            return head

