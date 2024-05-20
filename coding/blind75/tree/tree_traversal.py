import sys
sys.path.append("./coding")

from typing import Optional
from blind75.tree.utils_tree import TreeNode, traverse, generate_binary_tree_from_dict


if __name__ == "__main__":

    tree_dict = {
        3: (9, 20),
        20: (15, 7)
    }

    tree = generate_binary_tree_from_dict(tree_dict)

    print("lnr")
    traverse(tree, traversal_type = "lnr")

    print("lrn")
    traverse(tree, traversal_type = "lrn")

    print("nlr")
    traverse(tree, traversal_type = "nlr")
