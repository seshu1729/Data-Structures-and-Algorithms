# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum = 0                      # Will store the digit value for the current node
        carry = 0                    # Stores carry from previous digit addition
        
        dummy_head = ListNode(0)     # Dummy head node to build the resulting linked list easily
        dummy_tail = dummy_head      # Tail pointer to append new nodes to the result list
        
        # Continue the loop as long as there is a node in l1, l2, or leftover carry
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0   # Get current digit from l1; if l1 is None, use 0
            val2 = l2.val if l2 else 0   # Get current digit from l2; if l2 is None, use 0
            
            # Add digits + carry.
            # divmod(total, 10) gives: new_carry AND digit_to_store
            carry, sum = divmod(val1 + val2 + carry, 10)
            
            # Create a new node with the computed digit (sum)
            dummy_tail.next = ListNode(sum)
            
            # Move the tail pointer to the new node
            dummy_tail = dummy_tail.next
            
            # Move to next node in both lists if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the linked list starting from the actual first node (next of dummy head)
        return dummy_head.next
