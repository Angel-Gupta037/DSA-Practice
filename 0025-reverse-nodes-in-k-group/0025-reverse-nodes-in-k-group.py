# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if there are at least k nodes
        count = 0
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        if count < k:
            return head  # Not enough nodes → return as is
        # Step 2: Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Step 3: Recursively reverse the rest
        head.next = self.reverseKGroup(curr, k)
        
        return prev
        