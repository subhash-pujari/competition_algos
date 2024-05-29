"""
Problem: https://leetcode.com/problems/same-tree/description/
Solution: https://leetcode.com/problems/same-tree/solutions/4782659/beats-100-users-c-java-python-javascript-explained/
"""

import sys

sys.path.append("./coding")

from blind75.tree.utils_tree import (
    TreeNode,
    generate_binary_tree_list,
)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


tree_1 = generate_binary_tree_list([10, 4, 5, 8, 9])
tree_2 = generate_binary_tree_list([10, 4, 5, 8, 9])

print(Solution().isSameTree(tree_1, tree_2))
