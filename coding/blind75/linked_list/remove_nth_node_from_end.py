"""
Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
Solution: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/4813340/beat-100-00-full-explanation-with-pictures/
"""

import sys
sys.path.append("./")

from typing import Optional

from blind75.linked_list.utils import ListNode, generate_list, print_linked_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


if __name__ == "__main__":

    reduced_list = Solution().removeNthFromEnd(generate_list([1,2,3,4,5]), 2)
    
    print_linked_list(reduced_list)

    reduced_list = Solution().removeNthFromEnd(reduced_list, 1)

    print_linked_list(reduced_list)