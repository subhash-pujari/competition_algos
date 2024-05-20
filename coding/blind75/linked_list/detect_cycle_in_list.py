import sys
sys.path.append("./coding")

from typing import Optional

from blind75.linked_list.utils import ListNode, generate_list

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        cur = head

        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next

        return False

# if __init__ == "__main":
head = generate_list([1,2,3,4,5])
# head = Solution().reverseList(head)

curr = head
while curr.next:
    print(curr.data)
    curr = curr.next

# curr.next = head.next.next   

value = Solution().hasCycle(head)
print(value)

