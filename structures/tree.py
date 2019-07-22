"""Class implementations of tree types."""

from node import DoubleNode


class BinarySearchTree:
    """
    Double node implementation of binary search tree. For helpful discussions
    of binary search trees see:

    https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html
    https://algs4.cs.princeton.edu/32bst/

    Parameters
    ----------
    data : non-iterable object or iterable, default None.
        If an object, instance is a tree with a single node and object
        stored at the root. If iterable, instance is a tree with
        len(iterable) nodes with stored values given by iterable. Data
        values should be objects of the same type and support the
        python rich comparison methods:
        https://docs.python.org/3/reference/datamodel.html

    Attributes
    ----------
    root : DoubleNode
        Root node.
    left : DoubleNode
        Root node of left-hand subtree.
    left : DoubleNode
        Root node of right-hand subtree.

    """

    def __init__(self, data=None):
        if hasattr(data, '__iter__'):
            # Iterator for data
            data_iter = iter(data)
            # Set root node and current node to first data value
            self.root = curr = DoubleNode(next(data_iter))
            # iteratively build rest of tree from rest of data
            for elt in data_iter:
                if elt <= curr.data:
                    curr.left = DoubleNode(elt)
        else:
            self.root = DoubleNode(data=data)

    def _depth_first_traversal(self):
        pass

    def _breadth_first_traversal(self):
        pass

    def insert(self, data):
        pass

    def delete(self, data):
        pass

    def search(self, data):
        pass

    def min_val(self):
        pass

    def max_val(self):
        pass

    def min_val(self):
        pass

    def select(self):
        pass

    def rank(self):
        pass

    def height(self):
        pass
