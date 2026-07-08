class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.middle(head)
        right = mid.next
        mid.next = None
        left = head
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeLL(left, right)
    
    def middle(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeLL(self, l1, l2):
        dummy = ListNode(-1)
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:  
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        return dummy.next