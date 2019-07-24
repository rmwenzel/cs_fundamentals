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
        values should be objects of the same type and support rich
        comparison methods:

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
        return self._root

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

    def inorder_traversal(self, node):
        """
        Depth-first traversal of tree in order.

        Parameters
        ----------
        node: DoubleNode
            Node to begin traveral from.


        Returns
        -------
        data: list
            Sorted list of values.

        """
        data = []
        # recurse on non-empty left node
        if node.left:
            left_res = self.inorder_traversal(node.left)
            # flatten nested list
            for item in left_res:
                if isinstance(item, list):
                    for elt in item:
                        data += [elt]
                else:
                    data += [item]
        # include data if node is non-empty
        if node.data:
            data += [node.data]
        # recurse on non-empty right node
        if node.right:
            right_res = self.inorder_traversal(node.right)
            # flatten nested list
            for item in right_res:
                if isinstance(item, list):
                    for elt in item:
                        data += [elt]
                else:
                    data += [item]
        return data

    def search(self, node, data):
        """
        Search tree for data after node.

        Parameters
        ----------
        data: object
            Value to search for. Should support rich comparison.
        node: DoubleNode
            Node to begin search from.

        Raises
        ------
        ValueError
            Tree is empty
            Data not found

        Returns
        -------
        result: DoubleNode
            Node in tree containing data if found.

        """
        # Raise error if tree is empty
        if not node.data:
            raise ValueError("Tree is empty")
        # Base case: return node if data is found
        elif node.data == data:
            result = node
            return result
        else:
            # If data is left of node
            if data <= node.data:
                # Recurse if left node is non-empty
                if node.left:
                    result = self.search(node.left, data)
                    return result
                else:
                    raise ValueError(f"{data} not found in tree")
            # If data is right of node
            else:
                if node.right:
                    # Recurse if right node is non-empty
                    result = self.search(node.right, data)
                    return result
                else:
                    raise ValueError(f"{data} not found in tree")

    def min_val(self, node):
        """
        Find minimum value at or below node.

        Parameters
        ----------
        node: DoubleNode
            Node to begin searching from

        Raises
        ------
        ValueError
            Empty node

        Returns
        -------
        min_val: object
            Minimum value found at or below node

        """
        if not node.data:
            raise ValueError('Node is empty')
        # Move left until reaching a null pointer
        while True:
            if node.left:
                node = node.left
            else:
                min_val = node.data
                return min_val

    def max_val(self, node):
        """
        Find maximum value at or below node.

        Parameters
        ----------
        node: DoubleNode
            Node to begin searching from

        Raises
        ------
        ValueError
            Empty node

        Returns
        -------
        max_val: object
            Maximum value found at or below node

        """
        if not node.data:
            raise ValueError('Node is empty')
        # Move left until reaching a null pointer
        while True:
            if node.right:
                node = node.right
            else:
                max_val = node.data
                return max_val

    def delete(self, node, data):
        """
        Delete node containing data.

        Parameters
        ----------
        data: object
            Value to delete. Should be of same type as values already in
            tree and support rich comparison methods:

            https://docs.python.org/3/reference/datamodel.html
        node: DoubleNode
            Node to begin search from.

        """
        pass

    def select(self):
        pass

    def rank(self):
        pass


if __name__ == '__main__':
    import random
    sample = random.sample(range(1, 1001), 100)
    bst = BinarySearchTree(sample)
    res = bst.min_val(bst.root)
