# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res = []
        

        curr = head
        while curr:
            if curr in res:
                return True
            else:
                res.append(curr)
            curr = curr.next
        return False

