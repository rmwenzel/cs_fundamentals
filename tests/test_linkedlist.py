"""Unit tests for linked list classes."""

import pytest
from structures.linkedlist import SinglyLinkedList
from structures.node import SingleNode


class TestSinglyLinkedList:
    """Tests for SinglyLinkedList class."""

    @pytest.fixture
    def single_list_empty_node_data(scope='class'):
        """List constructed with one node with empty node as data."""
        d = SingleNode()
        sll = SinglyLinkedList(d)
        return d, sll

    @pytest.fixture
    def iter_list_int_data(scope='class'):
        """List constructed with iterable of ints."""
        return SinglyLinkedList(range(10))

    @pytest.fixture
    def split_list(scope='class'):
        """List of ints split in the middle."""
        int_list = list(range(10))
        sll = SinglyLinkedList(int_list[:5])
        return int_list[:5], int_list[5:], sll

    def test_empty_node_data_head(self, single_list_empty_node_data):
        """Head of list with single empty node has correct value."""
        d, sll = single_list_empty_node_data
        assert sll.head.data == d

    def test_empty_node_data_tail(self, single_list_empty_node_data):
        """Tail of list with single empty node has correct value."""
        d, sll = single_list_empty_node_data
        assert sll.tail.data == d

    def test_iterable_data_head(self, iter_list_int_data):
        """Head of list constructed from range object has correct value."""
        sll = iter_list_int_data
        assert sll.head.data == 0

    def test_iterable_data_tail(self, iter_list_int_data):
        """Tail of list constructed from range object has correct value."""
        sll = iter_list_int_data
        assert sll.tail.data == 9

    def test_iterator(self, iter_list_int_data):
        """List iterator returns correct values."""
        sll = iter_list_int_data
        curr = sll.head
        for node in sll:
            assert node == curr
            curr = curr.next_node

    def test_iterable_data(self, iter_list_int_data):
        """List constructed from iterable has correct values."""
        sll = iter_list_int_data
        for (i, node) in enumerate(sll):
            assert i == node.data

    def test_len(self, iter_list_int_data):
        """List constructed from iterable has correct length."""
        sll = iter_list_int_data
        assert len(sll) == 10

    def test_data_list(self, iter_list_int_data):
        """data_list returns correct value."""
        sll = iter_list_int_data
        assert sll.data_list() == list(range(10))

    def test_append_len(self, split_list):
        """List has correct length after append."""
        l1, l2, sll = split_list
        sll.append(l2)
        assert len(l1 + l2) == len(sll)

    def test_append_data(self, split_list):
        """List has correct data after append."""
        l1, l2, sll = split_list
        sll.append(l2)
        assert l1 + l2 == sll.data_list()

    def test_prepend_len(self, split_list):
        """List has correct length after prepend."""
        l1, l2, sll = split_list
        sll.prepend(l2)
        assert len(l1 + l2) == len(sll)

    def test_prepend_data(self, split_list):
        """List has correct data after prepend."""
        l1, l2, sll = split_list
        sll.prepend(l2)
        assert l2 + l1 == sll.data_list()

    def test_get_node(self, iter_list_int_data):
        """Method get_node returns correct value."""
        sll = iter_list_int_data
        for node in sll:
            if node.data == 5:
                get = node
        assert get == sll.get_node(5)

    def test_update_rightnode(self, iter_list_int_data):
        """Method update updates correct node."""
        sll = iter_list_int_data
        node = sll.get_node(5)
        sll.update(-1, node)
        assert node == sll.get_node(-1)

    def test_update_rightdata(self, iter_list_int_data):
        """Method update updates correct node."""
        sll = iter_list_int_data
        node = sll.get_node(5)
        sll.update(-1, node)
        assert node == sll.get_node(-1)

    def test_delete_len(self, iter_list_int_data):
        """Method delete results in list of correct length."""
        sll = iter_list_int_data
        node = sll.get_node(5)
        sll.delete(node)
        assert len(sll) == 9

    def test_delete_data(self, iter_list_int_data):
        """Method delete results in list of correct data."""
        sll = iter_list_int_data
        node = sll.get_node(5)
        sll.delete(node)
        int_list = list(range(10))
        int_list.remove(5)
        assert int_list == sll.data_list()
