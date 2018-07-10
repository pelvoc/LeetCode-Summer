# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        num = len(lists)
        interval = 1        
        while interval < num:
            for i in range(0 , num - interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        if num > 0:
            return lists[0]
        else:
            lists

    def merge2Lists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val: 
            l1.next = self.merge2Lists(l1.next, l2)
            return l1
        else: 
            l2.next = self.merge2Lists(l1, l2.next)
            return l2
