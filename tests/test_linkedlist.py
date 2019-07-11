"""
Unit tests for linked list classes

"""
import pytest
import linkedlist as ll


class TestSinglyLinkedList:
    """Tests for singly-linked list class."""

    def test_construct_singlenode_head(self):
        d = ll.SingleNode()
        sll = ll.SinglyLinkedList(d)
        assert sll.head.data == d

    def test_construct_singlenode_tail(self):
        d = ll.SingleNode()
        sll = ll.SinglyLinkedList(d)
        assert sll.tail.data == d

    def test_construct_iterable_head(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        assert sll.head.data == 0

    def test_construct_iterable_tail(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        assert sll.tail.data == 2

    def test_construct_iterable_data(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        for (i, node) in enumerate(sll):
            assert i == node.data

    def test_iterator(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        curr = sll.head
        for node in sll:
            assert curr == node
            curr = curr.next_node

    def test_len(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        assert len(sll) == 3

    def test_data_list(self):
        dlist = [1, 2, 3]
        sll = ll.SinglyLinkedList(dlist)
        assert dlist == sll.data_list()

    def test_append_len(self):
        l1, l2 = [1, 2, 3], [4, 5, 6]
        sll = ll.SinglyLinkedList(l1)
        sll.append(l2)
        assert len(l1 + l2) == len(sll)

    def test_append_data(self):
        l1, l2 = [1, 2, 3], [4, 5, 6]
        sll = ll.SinglyLinkedList(l1)
        sll.append(l2)
        assert l1 + l2 == sll.data_list()

    def test_prepend_len(self):
        l1, l2 = [1, 2, 3], [4, 5, 6]
        sll = ll.SinglyLinkedList(l1)
        sll.prepend(l2)
        assert len(l1 + l2) == len(sll)

    def test_prepend_data(self):
        l1, l2 = [1, 2, 3], [4, 5, 6]
        sll = ll.SinglyLinkedList(l1)
        sll.prepend(l2)
        assert l2 + l1 == sll.data_list()

    def test_get_node(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        for node in sll:
            if node.data == 1:
                get = node
        assert get == sll.get_node(1)

    def test_update_rightnode(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        node = sll.get_node(1)
        sll.update(4, node)
        assert node == sll.get_node(4)

    def test_update_rightdata(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        node = sll.get_node(1)
        sll.update(4, node)
        assert node.data == sll.get_node(4).data

    def test_delete_len(self):
        r = range(3)
        sll = ll.SinglyLinkedList(r)
        node = sll.get_node(1)
        sll.delete(node)
        assert len(sll) == len(r) - 1

    def test_delete_data(self):
        dl = [0, 1, 2]
        sll = ll.SinglyLinkedList(dl)
        node = sll.get_node(1)
        sll.delete(node)
        dl.remove(1)
        assert dl == sll.data_list()

