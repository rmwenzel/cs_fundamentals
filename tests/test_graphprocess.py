"""Unit tests for graph processing methods."""

import pytest
from algorithms.graphprocess import DirGraphProcess
from structures.graph import Vertex, Path


class TestDirGraphProcess:
    """Tests for DirGraphProcess class."""

    @pytest.fixture
    def city_graph(scope='class'):
        """Graph of vertices with city names as data and no edges."""
        names = ['Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles']
        vertices = [Vertex(name) for name in names]
        g = DirGraphProcess({vertex: [] for vertex in vertices})

        edges = [('Boston', 'Providence'), ('Boston', 'New York'),
                 ('Providence', 'Boston'), ('Providence', 'New York'),
                 ('New York', 'Chicago'), ('Chicago', 'Phoenix'),
                 ('Chicago', 'Denver'), ('Denver', 'Phoenix'),
                 ('Denver', 'New York'), ('Los Angeles', 'Boston')]
        for edge in edges:
            city1, city2 = edge
            g.addedge(g.v(city1), g.v(city2))
        return g

    def test_dfs_rec_shortpath_1(self, city_graph):
        """Check shortest path is correct."""
        # get shortest path results
        g = city_graph
        v1, v2 = g.v('Boston'), g.v('Phoenix')
        shortpath = g.dfs_rec_shortpath(v1, v2)
        # create correct path
        truepath = "['Boston', 'New York', 'Chicago', 'Phoenix']"
        assert str(shortpath) == truepath

    def test_dfs_rec_shortpath_2(self, city_graph):
        """Check shortest path returns None if no path."""
        # get shortest path results
        g = city_graph
        v1, v2 = g.v('Boston'), g.v('Los Angeles')
        shortpath = g.dfs_rec_shortpath(v1, v2)
        # create correct path
        truepath = None
        assert shortpath == truepath

    def test_dfs_it_shortpath_1(self, city_graph):
        """Check shortest path is correct."""
        # get shortest path results
        g = city_graph
        v1, v2 = g.v('Boston'), g.v('Phoenix')
        shortpath = g.dfs_rec_shortpath(v1, v2)
        # create correct path
        truepath = "['Boston', 'New York', 'Chicago', 'Phoenix']"
        assert str(shortpath) == truepath

    def test_dfs_it_shortpath_2(self, city_graph):
        """Check shortest path returns None if no path."""
        # get shortest path results
        g = city_graph
        v1, v2 = g.v('Boston'), g.v('Los Angeles')
        shortpath = g.dfs_rec_shortpath(v1, v2)
        # create correct path
        truepath = None
        assert shortpath == truepath

    def test_bfs_it_shortpath_1(self, city_graph):
        """Check shortest path is correct."""
        # get shortest path results
        g = city_graph
        v1, v2 = g.v('Boston'), g.v('Phoenix')
        shortpath = g.dfs_rec_shortpath(v1, v2)
        # create correct path
        truepath = "['Boston', 'New York', 'Chicago', 'Phoenix']"
        assert str(shortpath) == truepath

    def test_bfs_it_shortpath_2(self, city_graph):
        """Check shortest path returns None if no path."""
        # get shortest path results
        g = city_graph
        v1, v2 = g.v('Boston'), g.v('Los Angeles')
        shortpath = g.dfs_rec_shortpath(v1, v2)
        # create correct path
        truepath = None
        assert shortpath == truepath

    def test_dfs_rec_traversal_1(self, city_graph):
        """Check traversal is correct."""
        # get shortest path results
        g = city_graph
        boston = g.v('Boston')
        reachable = g.dfs_rec_traversal(start=boston, reachable=set())
        # create correct path
        names = {'Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix'}
        true_reachable = {g.v(name) for name in names}
        assert reachable == true_reachable

    def test_dfs_rec_traversal_2(self, city_graph):
        """Check traversal is correct."""
        # get shortest path results
        g = city_graph
        phoenix = g.v('Phoenix')
        reachable = g.dfs_rec_traversal(start=phoenix, reachable=set())
        # create correct path
        true_reachable = {phoenix}
        assert reachable == true_reachable
