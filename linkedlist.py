"""Class implementations of linked lists."""


class SingleNode:
    """
    Simple node class for use in singly-linked lists.

    Parameters
    ----------
    data : obj, default None
        The data to be stored in the node. Can be any object.

    Attributes
    ----------
    data : obj
        Object stored in the node.
    next : SingleNode
        Pointer to next node.

    """

    def __init__(self, data=None):
        self.data = data
        self.next = None
