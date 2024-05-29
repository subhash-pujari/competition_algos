import sys

sys.path.append("./coding")


from blind75.linked_list.utils import generate_list


list_obj = generate_list([1, 2, 3, 4])

slow = None
fast = None
