"""Implementations of node types."""


class SingleNode:
    """
    Simple single node class.

    Parameters
    ----------
    data : obj, default None
        The data to be stored in the node. Can be any object.

    Attributes
    ----------
    data : obj
        Object stored in the node.
    next_node : SingleNode
        Pointer to next node.

    """

    def __init__(self, data=None, next_node=None):
        """Class constructor."""
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Get, set, or delete node data."""
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @data.deleter
    def data(self):
        del self._data

    @property
    def next_node(self):
        """Get, set, or delete left node."""
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node

    @next_node.deleter
    def next_node(self):
        del self._next_node


class DoubleNode:
    """
    Simple double node class.

    Parameters
    ----------
    data : obj, default None
        The data to be stored in the node. Can be any object.

    Attributes
    ----------
    data : obj
        Object stored in the node.
    left : DoubleNode
        Left-hand node,
    right: DoubleNode
        Right-hand node,

    """

    def __init__(self, data=None, left=None, right=None):
        """Class constructor."""
        self._data = data
        self._left = left
        self._right = right

    @property
    def data(self):
        """Get, set, or delete node data."""
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @data.deleter
    def data(self):
        del self._data

    @property
    def left(self):
        """Get, set, or delete left node."""
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @left.deleter
    def left(self):
        del self._left

    @property
    def right(self):
        """Get, set, or delete right node."""
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @right.deleter
    def right(self):
        del self._right

