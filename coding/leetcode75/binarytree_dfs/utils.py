class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree_nodes = [3, 1, 4, 3, None, 1, 5]


def generate_tree(tree_nodes):
    if not tree_nodes:
        return None
    root = TreeNode(tree_nodes[0])
    nodes = [root]
    i = 1
    while i < len(tree_nodes):
        node = nodes.pop(0)
        if tree_nodes[i] is not None:
            node.left = TreeNode(tree_nodes[i])
            nodes.append(node.left)
        i += 1
        if i < len(tree_nodes) and tree_nodes[i] is not None:
            node.right = TreeNode(tree_nodes[i])
            nodes.append(node.right)
        i += 1
    return root


def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
