# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        l = []
        while head:
            l.append(head.val)
            head = head.next
        left = 0
        right = len(l) - 1
        while left <= right:
            if l[left] != l[right]:
                return False
            left = left + 1
            right = right - 1
        return True