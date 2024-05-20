"""
Problem : https://leetcode.com/problems/merge-two-sorted-lists/description/
Solution From: https://leetcode.com/problems/merge-two-sorted-lists/solutions/5111386/video-using-dummy-pointer-and-recursion-solution-as-a-bonus/
"""

import sys
sys.path.append("./coding")

from typing import Optional

from blind75.linked_list.utils import ListNode, generate_list, print_linked_list

class Solution_1:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-float("inf"))
        cur = dummy

        while list1 and list2:
            if list1.data > list2.data:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next


if __name__ == "__main__":
    list_1 = generate_list([1,2,4])
    list_2 = generate_list([1,3,4])

    list_head = Solution_1().mergeTwoLists(list_1, list_2)

    print("solution 1")
    print_linked_list(list_head)

    # list_head = Solution_2().mergeTwoLists(list_1, list_2)

    # print("solution 2")
    # print_linked_list(list_head)
    