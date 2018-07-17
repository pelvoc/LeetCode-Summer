# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None: return False
        w=head
        r=head
        
        while r.next is not None and r.next.next is not None:
            w=w.next
            r=r.next.next
            if w==r: 
                return True
        
        return False