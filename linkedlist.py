"""
Class implementations of linked lists.

For a helpful discussion of singly-linked lists with Java code see:
https://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/linked%20lists.html

"""


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
    next_node : SingleNode
        Pointer to next node.

    """

    def __init__(self, data=None):
        """Class constructor."""
        self.data = data
        self.next_node = None


class SinglyLinkedList:
    """
    Singly-linked list class.

    Parameters
    ----------
    data : non-iterable object or iterable, default None.
        If an object, instance is linked list with a single node and object
        as stored value. If iterable, instance is a linked-list with
        len(iterable) nodes with stored values given by iterable.

    Attributes
    ----------
    head : SingleNode.
        Head node of singly-linked list.
    tail : SingleNode, default None.
        Tail node of singly-linked list.

    """

    def __init__(self, data=None):
        """Class constructor."""
        # If no data is passed
        if not data:
            # Set head and tail to be the same empty single node
            self.head = self.tail = SingleNode()
        # If data is an iterable
        elif hasattr(data, '__iter__'):
            # Iterator for data
            data_iter = iter(data)
            # Set head node value to be first value in data
            self.head = SingleNode(next(data_iter))
            # Pointer to current node
            curr = self.head
            # Iteratively build nodes and move pointer
            for elt in data_iter:
                curr.next_node = SingleNode(elt)
                curr = curr.next_node
            # Set tail to last node pointer
            self.tail = curr
        # Else data is not an iterable
        else:
            # Set head node with data
            self.head = SingleNode(data)
            # Set tail node to last node pointer
            self.tail = self.head.next_node

    def __next__(self):
        if self.n:
            n = self.n
            self.n = self.n.next_node
            return n
        else:
            raise StopIteration

    def __iter__(self):
        # Next 
        self.n = self.head
        return self

    def __len__(self):
        count = 0
        for node in self.__iter__():
            count += 1
        return count

    def append(self, data):
        """
        Append data to end of list.

        Parameters
        ----------
        data : non-iterable object or iterable, default None.
            If an object, appends a single node with object as stored value.
            If iterable, appends len(iterable) nodes with stored values given
            by iterable.

        """
        # If data is an iterable
        if hasattr(data, '__iter__'):
            # Iteratable iterator
            data_iter = iter(data)

            # Set tail as current node
            curr = self.tail

            # Iterate over data adding nodes
            for elt in data_iter:
                curr.next_node = SingleNode(elt)
                temp = curr
                curr = curr.next_node
            self.tail = temp
        # Else data is an non-iterable
        else:
            self.tail.next_node = SingleNode(data)
            self.tail = self.tail.next_node

    def prepend(self, data):
        """
        Prepend data to beginning of list.

        Parameters
        ----------
        data : non-iterable object or iterable, default None.
            If object, prepends a single node with object as stored value.
            If iterable, prepends len(iterable) nodes with stored values
            given by iterable.

        """
        # Create new singly linked list with data
        sll = SinglyLinkedList(data)
        # Point tail to head of old list
        sll.tail.next_node = self.head
        # Point head of old list to head of new list
        self.head = sll.head

    def insert_after(self, key):
        pass

    def insert_before(self, key):
        pass

    def update(self, data):
        pass

    def delete(self, key):
        pass

    def data_list(self):
        pass


if __name__ == '__main__':

        sll = SinglyLinkedList([1, 2, 3])
        sll.prepend([3, 4, 5])
