"""
Problem: https://leetcode.com/problems/merge-k-sorted-lists/description/
Solution: https://leetcode.com/problems/merge-k-sorted-lists/solutions/3285930/100-faster-c-java-python/
"""

import sys
sys.path.append("./coding")

from typing import Optional, List

from blind75.linked_list.utils import ListNode, generate_list, print_linked_list

class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        
        return dummy.next


list_1 = generate_list([1,2,4])
list_2 = generate_list([1,3,4])
list_3 = generate_list([4,5,6])


list_head = Solution().mergeKLists([list_1, list_2, list_3])

print_linked_list(list_head)