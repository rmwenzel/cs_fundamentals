"""Linked list data structures."""

from structures.node import SingleNode


class SinglyLinkedList:
    """
    Node-based implementation of singly-linked lists.

    For a helpful discussion of singly-linked lists with Java code see:

    https://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/linked%20lists.html

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
            self.tail = self.head

    def __next__(self):
        """Next dunder."""
        # As long as self.n points to a node, return and increment
        if self.n:
            n = self.n
            self.n = self.n.next_node
            return n

        else:
            raise StopIteration

    def __iter__(self):
        """Iterate-or dunder."""
        # Attribute for next function
        self.n = self.head
        return self

    def __len__(self):
        """Length dunder."""
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
            # Iterable iterator
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
        new = SinglyLinkedList(data)
        # Point tail to head of old list
        new.tail.next_node = self.head
        # Point head of old list to head of new list
        self.head = new.head

    def get_node(self, key):
        """
        Get first node containing key.

        Parameters
        ----------
        key: object
            Value in node to get

        Returns
        -------
        node: SingleNode
            Node containing key

        """
        for node in self.__iter__():
            if node.data == key:
                return node

        raise ValueError('key not found')

    def insert(self, data, key):
        """
        Insert new nodes containing data after first node containing key.

        Parameters
        ----------
        data : non-iterable object or iterable, default None.
            If object, inserts a single node with object as stored value.
            If iterable, inserts len(iterable) nodes with stored values
            given by iterable.
        key: object
            Value in node after which data is inserted


        """
        # get node with key
        node = self.get_node(key)
        # create new list with data
        new = SinglyLinkedList(data)
        # point tail of new list to rest of old list
        new.tail.next_node = node.next_node
        # point first part of old list to head of new
        node.next_node = new.head

    def update(self, data, node):
        """
        Update single node with data.

        Parameters
        ----------
        data: non-iterable object
            New value to update node with
        node: SingleNode
            Node to update

        """
        node.data = data

    def delete(self, node):
        """
        Delete node from list.

        Parameters
        ----------
        node: SingleNode
            node to delete from list

        """
        # If we're deleting the head node
        if self.head == node:
            # Point head to next node
            self.head = node.next_node
            return None

        # If the node we're deleting occurs after head
        else:
            # iterate over one node back
            for prev in self.__iter__():
                # current node is next node of previous
                curr = prev.next_node
                # if this is the node we want to delete
                if curr == node:
                    # point previous next node to current next node
                    prev.next_node = curr.next_node
                    return None

        raise ValueError('Node not found')

    def data_list(self):
        """
        Get node values as list.

        Returns
        ----------
        data : list
            Node values

        """
        data = [node.data for node in self.__iter__() if node.data is not None]
        return data
