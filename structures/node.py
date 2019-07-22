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
        self.data = data
        self.next_node = next_node


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
        self.data = data
        self.left = left
        self.right = right
