# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        res = set()


        while head:
            if head in res:
                return True
            
            res.add(head)
            head = head.next
        return False

        