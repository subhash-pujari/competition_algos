"""
Problem: https://leetcode.com/problems/reorder-list/description/
Solution: https://leetcode.com/problems/reorder-list/solutions/4912096/beat-99-easy/
"""

import sys
sys.path.append("./coding")

from typing import Optional

from blind75.linked_list.utils import ListNode, generate_list, print_linked_list

class Solution(object):

    # Function for reversing
    def reverse(self, head):
        prev = None
        current = head
        while current:
            prev, prev.next, current = current, prev, current.next
        return prev
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        fast = head.next
        slow = head

        # Catch the Middle of List (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Cut Middle of list then Reverse it
        rev = self.reverse(slow.next)
        slow.next = None

        while rev:
            h_next = head.next
            r_next = rev.next
            head.next = rev
            rev.next = h_next
            rev = r_next
            head = h_next

        return head

# need to check this algorithm again
reordered_list = Solution().reorderList(generate_list([1,2,3,4,5]))
print_linked_list(reordered_list)