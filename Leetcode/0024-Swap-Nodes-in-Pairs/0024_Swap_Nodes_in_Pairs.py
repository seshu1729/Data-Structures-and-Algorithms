# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            dummy_node = ListNode(0)
            dummy_node.next = head
            head = dummy_node

            previous_node = head
            current_node = previous_node.next
            node_to_move = current_node.next

            while current_node is not None and current_node.next is not None:
                current_node.next = node_to_move.next
                node_to_move.next = previous_node.next
                previous_node.next = node_to_move

                previous_node = current_node
                current_node = previous_node.next
                if current_node is not None and current_node.next is not None:
                    node_to_move = current_node.next
            head = dummy_node.next
            return head


