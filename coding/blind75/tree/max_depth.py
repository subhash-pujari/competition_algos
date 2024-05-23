"""
Solution: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

import sys
sys.path.append("./coding")

from typing import Optional
from blind75.tree.utils_tree import TreeNode, traverse, generate_binary_tree_from_dict


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


if __name__ == "__main__":

    tree_dict = {
        3: (9, 20),
        20: (15, 7),
        15: (3, 4),
    }

    print(Solution().maxDepth(generate_binary_tree_from_dict(tree_dict)))
