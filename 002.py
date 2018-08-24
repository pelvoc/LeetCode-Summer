# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1=l1
        c2=l2
    
        sentinel=ListNode(0)
        d=sentinel
        
        sums=0

        while c1!=None or c2!=None:
            sums/=10
            if c1!=None:
                sums+=c1.val
                c1=c1.next
            if c2!=None:
                sums+=c2.val
                c2=c2.next
            
            d.next=ListNode(sums%10)
            d=d.next
        
        if sums/10==1:
            d.next=ListNode(1)
        
        return sentinel.next 