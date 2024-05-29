import sys

sys.path.append("./coding")

from linked_list.utils import generate_list


class Solution(object):
    def reverseList(self, head):
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node


if __name__ == "__main__":
    head = generate_list([1, 2, 3, 4, 5])
    head = Solution().reverseList(head)

    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
