# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head

        t = length - (k%length)
        for _ in range(t):
            cur = cur.next
            
        newhead = cur.next
        cur.next = None
        return newhead   