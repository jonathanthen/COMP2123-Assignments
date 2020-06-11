"""
Tree
-------

This is the tree file, it holds the main data structure that will be used for
testing. The tree contains a root node which then has children until the
leaves.
This is the main file for the interaction of tests.

Your task is to implement the methods for put and flatten.
"""


class Tree:
    """
    Tree Class
    Holds nodes, where each node in the tree has children, unless it is a leaf,
    where it has 0 children.

    Each node in the tree is type <class Node> defined in `node.py`.

    - Init: Sets up the tree with the specified root node.
    - put(node, child): Adds the child node to the specified node in the tree.
    - flatten(node): flatten the node.
    """

    def __init__(self, root):
        """
        Initialises the tree with a root node.
        :param root: the root node.
        """
        self.root = root

    def put(self, node, child):
        """
        Inserts a node into the tree. Adds `child` to `node`.
        :param node: The node currently in the tree.
        :param child: The child to add to the tree.
        """

        node.add_child(child)

    def _propagate_values(self, current_node, value):
        """
        Recursively propagates values of the "subtree" upwards.
        :param current_node: The node to propagate
        :param value: int The value we are comparing against.
        """

        # Check the children and current node
        subtree_max = current_node.key
        if len(current_node.children) > 0:
            subtree_max = max([current_node.key] + [i.subtree_value for i in current_node.children])

        # If it's greater, then we terminate.
        if subtree_max > value:
            value = subtree_max

        # Change the value
        current_node.subtree_value = value

        # We are at the root
        if current_node.parent is None:
            return

        # Recursively propagate upwards
        self._propagate_values(current_node.parent, value)

    def _recursive_flatten(self, node):
        """
        Internal function to recursively go through and flatten nodes.
        If the node is a leaf node, it terminates the recursion and returns.
        :param node: The node to be flattened.
        :return: The summed value of the nodes that are flattened.
        """

        # let's get recursive
        if node.is_external():
            return node.key

        node_sum = node.key

        for i in node.children:
            node_sum += self._recursive_flatten(i)

        node.children = []

        return node_sum

    def flatten(self, node):
        """
        Flatten the node given by removing the subtree rooted at this node.
        You must (a) flatten the subtree, (b) compute the sum of all nodes
        below and perform any updates
        to other nodes.

        Example
        flatten(subtree_root) = subtree_root.key = sum(subtree_root)

        :param node: The root of the subtree to flatten.
        :return:
        """

        node_sum = self._recursive_flatten(node)
        node.key = node_sum

        self._propagate_values(node, node_sum)

    def swap(self, subtree_a, subtree_b):
        """
        Swap subtree A with subtree B
        :param subtree_a: The root node of subtree_a.
        :param subtree_b: The root node of subtree_b.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        tree.swap(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """

        # Get the parent.
        parent_a = subtree_a.parent
        parent_b = subtree_b.parent

        # Remove subtree from parents, add to other.
        del(parent_a.children[
            parent_a.children.index(subtree_a)
        ])
        del(parent_b.children[
            parent_b.children.index(subtree_b)
        ])

        parent_a.add_child(subtree_b)
        parent_b.add_child(subtree_a)

        subtree_b.parent = parent_a
        subtree_a.parent = parent_b

        # Bubble up the values for a and b
        parent_a.subtree_value = parent_a.key
        parent_b.subtree_value = parent_b.key

        max_value = max([i.subtree_value for i in parent_a.children])
        self._propagate_values(parent_a, max_value)

        max_value = max([i.subtree_value for i in parent_b.children])
        self._propagate_values(parent_b, max_value)
