# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        slow = head
        while slow is not None:
            fast = slow.next
            while fast is not None:
                if slow.val == fast.val:
                    slow.next = fast.next
                fast = fast.next
            slow = slow.next
        return temp