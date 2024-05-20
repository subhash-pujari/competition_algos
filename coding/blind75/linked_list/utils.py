class ListNode:
    def __init__(self, num) -> None:
        self.next = None
        self.data = num


def generate_list(nums):
    prev = None
    for num in nums:
        node = ListNode(num)
        if prev:
            prev.next = node
        else:
            head = node
        prev = node
    return head


def print_linked_list(list_head):
    curr = list_head
    while curr:
        print(curr.data)
        curr = curr.next