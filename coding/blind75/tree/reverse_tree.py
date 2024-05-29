"""
Problem: https://leetcode.com/problems/invert-binary-tree/description/
Solution: https://leetcode.com/problems/invert-binary-tree/solutions/2463600/easy-100-fully-explained-java-c-python-js-c-python3-recursive-iterative/
"""

import sys

sys.path.append("./coding")

from blind75.tree.utils_tree import (
    traverse,
    generate_binary_tree_list,
)


class Solution(object):
    def invertTree(self, root):
        # Base case...
        if root is None:
            return root
        # swapping process...
        root.left, root.right = root.right, root.left
        # Call the function recursively for the left subtree...
        self.invertTree(root.left)
        # Call the function recursively for the right subtree...
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    tree = generate_binary_tree_list([3, 9, 20, 15, 7])

    traverse(tree, "lnr")

    tree = Solution().invertTree(tree)

    print("After revert")

    traverse(tree, "lnr")
