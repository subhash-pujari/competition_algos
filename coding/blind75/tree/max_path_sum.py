"""
problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
solution: https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

import sys

sys.path.append("./coding")

from typing import Optional
from blind75.tree.utils_tree import (
    TreeNode,
    generate_binary_tree_list,
)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]

        def DFS(root):
            if root is None:
                return 0

            lmax = DFS(root.left)
            rmax = DFS(root.right)
            lmax = 0 if lmax < 0 else lmax
            rmax = 0 if rmax < 0 else rmax

            ans[0] = max(ans[0], root.val + lmax + rmax)

            return root.val + max(lmax, rmax)

        DFS(root)
        return ans[0]


if __name__ == "__main__":
    tree = generate_binary_tree_list([3, 9, 1, 15, 7])

    print(Solution().maxPathSum(tree))
