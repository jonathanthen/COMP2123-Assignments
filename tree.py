"""
Tree
-------

This is the tree file, it holds the main data structure that will be used for
testing. The tree contains a root node which then has children until the
leaves.
This is the main file for the interaction of tests.

Your task is to implement the methods for put and flatten.
"""
import node

class Tree:
    """
    Tree Class
    Holds nodes, where each node in the tree has children, unless it is a leaf,
    where it has 0 children.

    Each node in the tree is type <class Node> defined in `node.py`.

    - Init: Sets up the tree with the specified root node.
    - put(node, child): Adds the child node to the specified node in the tree.
    - flatten(node): flatten the node.
    - swap(subtree_a, subtree_b): Swap the position of the subtrees.
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
        child.parent = node
        node.add_child(child)


    def flatten(self, node):
        """
        Flatten the node given by removing the subtree rooted at this node.
        You must (a) flatten the subtree, (b) compute the sum of all nodes
        below and perform any updates
        to other nodes.

        :param node: The root of the subtree to flatten.

        Example

           A(5)
           / \
         B(3) C(6)
         /    |  \
        D(2) E(3) F(6)

        flatten(C)

           A(5)
           / \
         B(3) C(15)
         /
        D(2)

        """
        if node.is_external():
            return

        total = node.countKey(node) #RECURSION FUNCTION THAT
                                    #RETURNS AN ARRAY OF ALL KEYS
        t = 0
        i = 0
        while i < len(total): 
            t += total[i]
            i+=1

        #DELETING CHILD NODES
        while len(node.children) != 0:
            del node.children[0]

        node.key = t
        node.subtree_value = t

        #CHANGE ALL PARENTS SUBTREE VALUES
        n = node
        nval = n.subtree_value

        while n.parent != None:
            if n.parent.subtree_value < nval:
                n.parent.subtree_value = nval
            n = n.parent



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

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """

        if subtree_a.parent == None or subtree_b.parent == None:
            return

        temp = subtree_a.parent

        subtree_a.parent = subtree_b.parent #CHANGE A PARENT TO B PARENT
        subtree_b.parent.add_child(subtree_a) #ADD CHILD
        subtree_b.parent.children.remove(subtree_b) #REMOVE EXISTING CHILD
        temp.add_child(subtree_b) #ADD CHILD
        temp.children.remove(subtree_a) #REMOVE EXISTING CHILD
        subtree_b.parent = temp #CHANGE B PARENT TO A

        #UPDATING SUBTREE VALUES

        n = subtree_a

        while n.parent != None:
            if n.parent.subtree_value <= n.subtree_value:
                n.parent.subtree_value = n.subtree_value
            else:
                if n.parent.parent == None:
                    break
                else:
                    if n.parent.subtree_value != n.parent.key:
                        if n.parent.key < n.subtree_value:
                            n.parent.subtree_value = n.subtree_value
                        else:
                            n.parent.subtree_value = n.parent.key

            n = n.parent


        n = subtree_b

        while n.parent != None:
            if n.parent.subtree_value <= n.subtree_value:
                n.parent.subtree_value = n.subtree_value
            else:
                if n.parent.parent == None:
                    break
                else:
                    if n.parent.subtree_value != n.parent.key:
                        if n.parent.key < n.subtree_value:
                            n.parent.subtree_value = n.subtree_value
                        else:
                            n.parent.subtree_value = n.parent.key

            n = n.parent