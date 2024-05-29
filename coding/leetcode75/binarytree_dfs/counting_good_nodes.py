import sys

sys.path.append("./")


from coding.leetcode75.binarytree_dfs.utils import generate_tree, tree_nodes

path_to_root = []

tree_modes = [3, 1, 4, 3, None, 1, 5]
root = generate_tree(tree_nodes)

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes)

# Example 1:
