# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
            current = head
            while current:
                values.append(current.val)
                current = current.next

                
        values.sort()

        head2 = ListNode(0)
        tail = head2
        for val in values:
            tail.next = ListNode(val)
            tail = tail.next

        return head2.next