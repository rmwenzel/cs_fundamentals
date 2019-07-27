"""Unit tests for tree classes."""

import pytest
from structures.tree import BinarySearchTree


class TestBinarySearchTree:
    """Tests for BinarySearchTree class."""

    @pytest.fixture
    def one_node_tree(scope='class'):
        """Tree with single node constructed from single value."""
        return BinarySearchTree(1)

    @pytest.fixture
    def two_node_tree(scope='class'):
        """Tree with two nodes constructed from range object."""
        return BinarySearchTree(range(1, 3))

    @pytest.fixture
    def three_node_tree(scope='class'):
        """Tree with three nodes constructed from list."""
        return BinarySearchTree([3, 1, 5])

    @pytest.fixture
    def large_tree_list(scope='class'):
        """List of node for large tree."""
        return [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]

    @pytest.fixture
    def large_tree(scope='class'):
        """
        12 node tree.

        Visualization can be found here:

        https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html

        """
        return BinarySearchTree([11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31])

    def test_one_node_tree_root(self, one_node_tree):
        """Root of single node tree has correct value."""
        bst = one_node_tree
        assert bst.root.data == 1

    def test_three_node_tree_data(self, three_node_tree):
        """Nodes of three node tree have correct values."""
        bst = three_node_tree
        assert bst.root.data == 3
        assert bst.root.left.data == 1
        assert bst.root.right.data == 5

    def test_large_tree_data(self, large_tree):
        """Large tree has correct structure."""
        bst = large_tree
        assert bst.root.data == 11
        assert bst.root.left.data == 6
        assert bst.root.left.left.data == 4
        assert bst.root.left.left.right.data == 5
        assert bst.root.left.right.data == 8
        assert bst.root.left.right.right.data == 10
        assert bst.root.right.data == 19
        assert bst.root.right.left.data == 17
        assert bst.root.right.right.data == 43
        assert bst.root.right.right.left.data == 31
        assert bst.root.right.right.right.data == 49

    def test_large_tree_traversal(self, large_tree, large_tree_list):
        """Method in order traversal returns nodes in correct order."""
        bst = large_tree
        bst_traverse_list = bst.inorder_traversal(bst.root)
        assert sorted(large_tree_list) == bst_traverse_list

    def test_large_tree_delete(self, large_tree):
        """Large tree has correct structure after delete."""
        bst = large_tree
        bst.delete(bst.root, 11)
        assert bst.root.data == 10
        assert bst.root.left.data == 6
        assert bst.root.left.left.data == 4
        assert bst.root.left.left.right.data == 5
        assert bst.root.left.right.data == 8
        assert bst.root.right.data == 19
        assert bst.root.right.left.data == 17
        assert bst.root.right.right.data == 43
        assert bst.root.right.right.left.data == 31
        assert bst.root.right.right.right.data == 49

    def test_large_tree_min(self, large_tree):
        """Method min_val returns correct value."""
        bst = large_tree
        assert bst.min_val(bst.root) == 4

    def test_large_tree_max(self, large_tree):
        """Method max_val returns correct value."""
        bst = large_tree
        assert bst.max_val(bst.root) == 49

    def test_large_tree_search_positive(self, large_tree):
        """Method search correctly detects value."""
        bst = large_tree
        node = bst.search(bst.root, 17)
        assert node.data == 17

    def test_large_tree_search_negative(self, large_tree):
        """Method search correctly detects value."""
        bst = large_tree
        with pytest.raises(ValueError):
            bst.search(bst.root, 100)
