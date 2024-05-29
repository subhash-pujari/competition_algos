import sys

sys.path.append("./")

from typing import Optional

from coding.leetcode75.binarytree_dfs.utils import TreeNode, generate_tree, print_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    vals = [3, 9, 20, None, None, 15, 7]
    root = generate_tree(vals)
    print_tree(root)
    print(Solution().maxDepth(root))
