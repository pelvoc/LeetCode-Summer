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
        s1=[]
        s2=[]
    
        while l1!=None: 
            s1.append(l1.val)
            l1=l1.next
            
        while l2!=None:
            s2.append(l2.val)
            l2=l2.next
            
        sums=0
        
        ls=ListNode(0)
    
        while s1 or s2:
            if s1:
                sums+=s1.pop()
            if s2:
                sums+=s2.pop()
            
            ls.val=sums%10    
            head=ListNode(sums/10)
            head.next=ls
            ls=head
            sums/=10
            
        return ls.next if ls.val==0 else ls