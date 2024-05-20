
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def traverse(root, traversal_type):

    if traversal_type == "lnr":

        if root:

            if root.left:
                traverse(root.left, "lnr")

            print(root.val)

            if root.right:
                traverse(root.right, "lnr")

    elif traversal_type == "lrn":

        if root:

            if root.left:
                traverse(root.left, "lrn")

            if root.right:
                traverse(root.right, "lrn")

            print(root.val)

    elif traversal_type == "nlr":

        if root:

            print(root.val)

            if root.left:
                traverse(root.left, "nlr")

            if root.right:
                traverse(root.right, "nlr")


def generate_binary_tree_from_dict(tree_dict):

    tree = None
    nodes = dict()

    for val in tree_dict:
        
        if val not in nodes:
            nodes[val] = TreeNode(val)        

        left, right = tree_dict[val]
        left_node = TreeNode(left)
        right_node = TreeNode(right)

        nodes[val].left = left_node
        nodes[val].right = right_node

        nodes[left] = left_node
        nodes[right] = right_node

        if tree is None:
            tree = nodes[val]

    return tree
