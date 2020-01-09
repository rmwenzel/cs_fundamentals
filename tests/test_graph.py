"""Unit tests for graph structures."""

import pytest
from structures.graph import Vertex, Path, DirGraph


class TestVertex:
    """Tests for Vertex class."""

    @pytest.fixture
    def boston_vertex(scope='class'):
        """Vertex with city name as data."""
        v = Vertex('Boston')
        return v

    def test_data_getter(self, boston_vertex):
        """Data attribute getter return correct value."""
        assert boston_vertex.data == 'Boston'

    def test_data_setter(self, boston_vertex):
        """Data attribute setter sets correct value."""
        boston_vertex.data = 'Seattle'
        assert boston_vertex.data == 'Seattle'

    def test_data_deleter(self, boston_vertex):
        """Data attribute deletes correctly."""
        del boston_vertex.data
        try:
            boston_vertex.data
        except Exception as e:
            assert isinstance(e, AttributeError)

    def test_str(self, boston_vertex):
        """__str__ returns correct value."""
        assert str(boston_vertex) == 'Boston'


class TestPath:
    """Tests for Path class."""

    @pytest.fixture
    def city_path_1(scope='class'):
        """Path of vertices with city names for vertex data."""
        names = ['Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles']
        vertices = [Vertex(name) for name in names]
        path = Path(vertices)
        return names, vertices, path

    @pytest.fixture
    def city_path_2(scope='class'):
        """Path of vertices with city names for vertex data."""
        names = ['Seattle', 'Vancouver', 'San Francisco']
        vertices = [Vertex(name) for name in names]
        path = Path(vertices)
        return names, vertices, path

    def test_vertices_getter(self, city_path_1):
        """Data attribute getter return correct value."""
        _, vertices, path = city_path_1
        assert path.vertices == vertices

    def test_vertices_setter(self, city_path_1, city_path_2):
        """Data attribute setter sets correct value."""
        _, _, path1 = city_path_1
        _, _, path2 = city_path_1
        path1.vertices = path2.vertices
        assert path1.vertices == path2.vertices

    def test_vertices_deleter(self, city_path_1):
        """Data attribute deletes correctly."""
        _, _, path = city_path_1
        del path.vertices
        try:
            path.vertices
        except Exception as e:
            assert isinstance(e, AttributeError)

    def test_str(self, city_path_1):
        """__str__ returns correct value."""
        names, _, path = city_path_1
        assert str(path) == str(names)

    def test_len(self, city_path_1):
        """__len__ returns correct value."""
        _, vertices, path = city_path_1
        assert len(vertices) == len(path)

    def test_iter(self, city_path_1):
        """__iter__ returns correct value."""
        _, vertices, path = city_path_1
        assert [v for v in iter(vertices)] == [v for v in iter(path)]

    def test_add(self, city_path_1, city_path_2):
        """__add__ returns correct value."""
        _, vertices1, path1 = city_path_1
        _, vertices2, path2 = city_path_2
        new_path = Path(vertices1 + vertices2)
        add_path = path1 + path2
        assert [v for v in add_path] == [v for v in new_path]

    def test_addvertex(self, city_path_1):
        """Add vertex correctly to middle of path."""
        _, _, path = city_path_1
        v = Vertex(['Seattle'])
        path.addvertex(2, v)
        assert path.vertices[2] == v

    def test_removevertex(self, city_path_1):
        """Remove vertex correctly."""
        _, vertices, path = city_path_1
        vertices.remove(vertices[2])
        path.removevertex(path.vertices[2])
        assert path.vertices == vertices


class TestDirGraph:
    """Tests for Directed graph class."""

    @pytest.fixture
    def city_graph_no_edges(scope='class'):
        """Graph of vertices with city names as data and no edges."""
        names = ['Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles']
        vertices = [Vertex(name) for name in names]
        adj = {vertex: [] for vertex in vertices}
        g = DirGraph(adj)
        return names, vertices, adj, g

    @pytest.fixture
    def city_graph(scope='class'):
        """Graph of vertices with city names as data and no edges."""
        names = ['Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles']
        vertices = [Vertex(name) for name in names]
        g = DirGraph({vertex: [] for vertex in vertices})

        edges = [('Boston', 'Providence'), ('Boston', 'New York'),
                 ('Providence', 'Boston'), ('Providence', 'New York'),
                 ('New York', 'Chicago'), ('Chicago', 'Phoenix'),
                 ('Chicago', 'Denver'), ('Denver', 'Phoenix'),
                 ('Denver', 'New York'), ('Los Angeles', 'Boston')]
        for edge in edges:
            city1, city2 = edge
            g.addedge(g.v(city1), g.v(city2))
        return names, vertices, edges, g

    def test_adj_getter(self, city_graph_no_edges):
        """Adjacency list attribute getter returns correct value."""
        _, vertices, adj, g = city_graph_no_edges
        assert g.adj == adj

    def test_adj_setter(self, city_graph_no_edges):
        """Adjacency list attribute setter sets correct value."""
        _, vertices, adj, _ = city_graph_no_edges
        g = DirGraph()
        g.adj = adj
        assert g.adj == adj

    def test_adj_deleter(self, city_graph_no_edges):
        """Adjacency list attribute deleter deletes correctly."""
        _, _, _, g = city_graph_no_edges
        del g.adj
        try:
            g.adj
        except Exception as e:
            assert isinstance(e, AttributeError)

    def test_vertices_getter(self, city_graph_no_edges):
        """Vertices attribute getter returns correct value."""
        _, vertices, _, g = city_graph_no_edges
        assert g.vertices == vertices

    def test_vertices_deleter(self, city_graph_no_edges):
        """Vertices attribute deleter deletes correctly."""
        _, vertices, _, g = city_graph_no_edges
        del g.vertices
        try:
            g.vertices
        except Exception as e:
            assert isinstance(e, AttributeError)

    def test_v(self, city_graph_no_edges):
        """Test correct vertex is returned."""
        _, vertices, _, g = city_graph_no_edges
        for vertex in vertices:
            name = vertex.data
            assert vertex == g.v(name)

    def test_addvertex(self, city_graph_no_edges):
        """Test correct vertex is returned."""
        _, vertices, edges, _ = city_graph_no_edges
        vertex = vertices[0]
        g = DirGraph()
        g.addvertex(vertex)
        assert vertex in g.vertices

    def test_addedge(self, city_graph_no_edges):
        """Test correct vertex is returned."""
        _, vertices, _, g = city_graph_no_edges
        vertex1, vertex2 = vertices[0], vertices[1]
        g.addedge(vertex1, vertex2)
        assert vertex2 in g.adj[vertex1]

    def test_children(self, city_graph):
        """Test correct children are returned."""
        _, _, edges, g = city_graph
        for vertex in g.vertices:
            children = [g.v(edge[1]) for edge in edges
                        if g.v(edge[0]) == vertex]
            assert children == g.children(vertex)

    def test_parents(self, city_graph):
        """Test correct children are returned."""
        _, _, edges, g = city_graph
        for vertex in g.vertices:
            parents = [g.v(edge[0]) for edge in edges
                       if g.v(edge[1]) == vertex]
            assert parents == g.parents(vertex)
