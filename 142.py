# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: return None

        w=head
        r=head
        isCycle=False
        while w is not None and r is not None: 
            w=w.next
            if r.next is None: return None
            r=r.next.next
            if w==r: 
                isCycle=True
                break
     
        if not isCycle: return None
        w=head
        while w is not r: 
            w=w.next
            r=r.next
            
        return w