"""
Merge k sorted linked lists and return it as
one sorted list. Analyze and describe its complexity.
"""

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
        if not lists:
            return None
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists)-1, 2):
                merged = self.merge(lists[i], lists[i+1])
                tmp.append(merged)
            if len(lists) % 2 == 1:
                tmp.append(lists[-1])
            lists = tmp
        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode(None)
        ptr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next
        ptr.next = l1 if l1 else l2
        return dummy.next

    def mergeKLists2(self, lists):
        from heapq import heappop, heapreplace, heapify
        dummy = ListNode(None)
        ptr = dummy
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if not n.next:
                heappop(h)
            else:
                heapreplace(h, (n.next.val, n.next))
            ptr.next = n
            ptr = prt.next
        return dummy.next
