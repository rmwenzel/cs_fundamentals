"""Class implementations of tree types."""

from node import DoubleNode


class BinarySearchTree:
    """
    Double node implementation of binary search tree.

    For helpful discussions
    of binary search trees see:

    https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html
    https://algs4.cs.princeton.edu/32bst/

    Parameters
    ----------
    data : non-iterable object or iterable, default None.
        If an object, instance is a tree with one DoubleNode and object
        stored at the root. If iterable, instance is a tree with
        len(iterable) nodes with stored values given by iterable. Data
        values should be objects of the same type and support the
        python rich comparison methods:
        https://docs.python.org/3/reference/datamodel.html

    Attributes
    ----------
    root : DoubleNode
        Root node.

    """

    def __init__(self, data=None):
        """Class constructor."""
        if hasattr(data, '__iter__'):
            # data iterable
            data_iter = iter(data)
            # set root node and current node as first node
            self._root = DoubleNode(next(data_iter))
            # iteratively build tree
            self.insert(self.root, data_iter)
        else:
            self._root = DoubleNode(data=data)

    @property
    def root(self):
        """Get, set, or delete root node of tree."""
        return self.root

    @root.setter
    def root(self, node):
        self._root = node

    @root.deleter
    def root(self):
        del self._root

    def insert(self, node, data):
        """
        Insert data in tree starting at node.

        Parameters
        ----------
        node: DoubleNode
            Node to insert data under
        data : non-iterable object or iterable.
            Data to insert

        """
        # if data is an iterable
        if hasattr(data, '__iter__'):
            for elt in data: 
                # if elt belongs to the left of node
                if elt <= node.data:
                    # if left pointer is nonnull recurse
                    if node.left:
                        self.insert(node.left, elt)
                    # if left pointer is null create a node
                    else:
                        node.left = DoubleNode(elt)
                # if elt belongs to the right of node
                else:
                    # if right pointer is nonnull recurse
                    if node.right:
                        self.insert(node.right, elt)
                    # if right pointer is null create a node
                    else:
                        node.right = DoubleNode(elt)
        # if data is not an iterable
        else:
            if data <= node.data:
                if node.left:
                    self.insert(node.left, data)
                else:
                    node.left = DoubleNode(data)
            else:
                if node.right:
                    self.insert(node.right, data)
                else:
                    node.right = DoubleNode(data)

    def _depth_first_traversal(self):
        pass

    def _breadth_first_traversal(self):
        pass

    def delete(self, data):
        pass

    def search(self, data):
        pass

    def min_val(self):
        pass

    def max_val(self):
        pass

    def select(self):
        pass

    def rank(self):
        pass
