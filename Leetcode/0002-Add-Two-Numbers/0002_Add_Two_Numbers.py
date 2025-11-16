# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_tail = dummy_head
        carry = 0
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            carry, sum = divmod(value1 + value2 + carry, 10)

            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

            dummy_tail.next = ListNode(sum)
            dummy_tail = dummy_tail.next


        return dummy_head.next