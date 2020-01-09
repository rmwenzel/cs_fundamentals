"""Graph data structures."""


class Vertex:
    """
    Simple vertex.

    Parameters
    ----------
    data : obj, default None
        The data to be stored in the vertex. Can be any object.

    Attributes
    ----------
    data : obj
        Object stored in the vertex.
    next_vertex : Vertex
        Pointer to next vertex.

    """

    def __init__(self, data):
        """Class constructor."""
        self._data = data

    def __str__(self):
        """Use node data as string representation."""
        return str(self.data)

    @property
    def data(self):
        """Get, set, or delete vertex data."""
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @data.deleter
    def data(self):
        del self._data


class Path:
    """
    Path of vertices in graph.

    Parameters
    ----------
    vertices : list, default None
        List of vertices in path

    Attributes
    ----------
    vertices : list, default None
        List of vertices in path

    """

    def __init__(self, vertices):
        """Class constructor."""
        self._vertices = vertices

    def __str__(self):
        """Use node data as string representation."""
        return str([str(vertex.data) for vertex in self.vertices])

    def __len__(self):
        """Length of list of vertices."""
        return len(self.vertices)

    def __iter__(self):
        """Iterate over vertices."""
        return iter(self.vertices)

    def __add__(self, other_path):
        """Concatenate paths."""
        return Path(self.vertices + other_path.vertices)

    @property
    def vertices(self):
        """Get, set, or delete vertices."""
        return self._vertices

    @vertices.setter
    def vertices(self, new_vertices):
        self._vertices = new_vertices

    @vertices.deleter
    def vertices(self):
        del self._vertices

    def addvertex(self, index, vertex):
        """Add vertex path.

        Parameters
        ----------
        vertex: Vertex
            Vertex to add to end of path.
        index: int, default -1
            Index to insert vertex, default end of path.
        """
        # check if this vertex is at end of path
        if vertex == self.vertices[-1]:
            raise ValueError('Vertex already at end of path')
        else:
            self.vertices.insert(index, vertex)

    def removevertex(self, vertex):
        """Remove vertex from path.

        Parameters
        ----------
        vertex: Vertex
            Vertex to remove from end of path.
        """
        # check if this vertex is not at end of path
        if vertex not in self.vertices:
            raise ValueError('Vertex not path')
        else:
            self.vertices.remove(vertex)


class DirGraph:
    """Directed graph in adjacency list format.

    Parameters
    ----------
    adj: dict, default None
        Adjacency dictionary. Keys are the vertices of the graph and values are
        lists of children

    Attributes
    ----------
    adj: dict, default empty
        Keys are the vertices of the graph and values are lists of children
    vertices: list
        List of vertices of the graph, default empty
    """

    def __init__(self, adj={}):
        """Class constructor."""
        self._adj = adj
        self._vertices = list(adj.keys())

    def __str__(self):
        """Use node data for string representation."""
        return str({str(vertex): [str(child) for child in self.adj[vertex]]
                   for vertex in self.adj})

    @property
    def adj(self):
        """Get, set, or delete adjacency dictionary."""
        return self._adj

    @adj.setter
    def adj(self, new_adj):
        self._adj = new_adj

    @adj.deleter
    def adj(self):
        del self._adj

    @property
    def vertices(self):
        """Get set or delete vertices."""
        return list(self.adj.keys())

    @vertices.deleter
    def vertices(self):
        del self._vertices

    def v(self, data):
        """Find vertices by data.

        Parameters
        ----------
        data: Object
            data located at desired vertex.

        Returns
        -------
        vertex: Vertex or list of Vertexs
            Vertex or Vertices with data or None if none found.
        """
        # add all vertices with data to list
        vertices = []
        for vertex in self.vertices:
            if vertex.data == data:
                vertices += [vertex]
        if len(vertices) == 0:
            raise ValueError(f'Vertex with data {data} not in graph')
        elif len(vertices) == 1:
            return vertices[0]
        else:
            return vertices

    def addvertex(self, vertex):
        """Add vertex to graph.

        Parameters
        ----------
        vertex: Vertex
            Vertex to add to graph. Has no children by default
        """
        # check if this vertex is already in graph
        if vertex in self.adj:
            raise ValueError('Duplicate vertex')
        else:
            self.adj[vertex] = []

    def addedge(self, parent, child):
        """Add edge to graph.

        Parameters
        ----------
        parent: Node
            Node edge starts from.
        child: Node
            Node edge ends at.
        """
        # check if parent and child vertices are in graph
        if parent not in self.vertices:
            raise ValueError('Parent vertex not in graph')
        if child not in self.vertices:
            raise ValueError('Child vertex not in graph')
        # add child to list for parent vertex in adj dict
        self.adj[parent].append(child)

    def children(self, vertex):
        """Get all children of vertex.

        Parameters
        ----------
        vertex: Vertex
            Vertex to get children of

        Returns
        -------
        children: list
            List of children of vertex, possibly empty
        """
        # check if vertex is in graph
        if vertex not in self.vertices:
            raise ValueError('Vertex not in graph')
        # return vertices children
        children = self.adj[vertex]
        return children

    def parents(self, vertex):
        """Get all parents of vertex.

        Parameters
        ----------
        vertex: Vertex
            Vertex to get parents of

        Returns
        -------
        children: list
            List of children of vertex, possibly empty
        """
        # check if vertex is in graph
        if vertex not in self.vertices:
            raise ValueError('Vertex not in graph')
        parents = []
        # iterate over all other vertices
        for other_vertex in self.vertices:
            # if vertex is a child, other vertex is a parent
            if vertex in self.children(other_vertex):
                parents += [other_vertex]
        return parents


class Graph(DirGraph):
    """Undirected graph in adjacency list format."""

    def addedge(self, parent, child):
        """Override parent class method.

        Each edge is added twice, once in each direction. In this way, every
        parent-child relationship between vertices is reversed and the graph
        becomes undirected.

        Parameters:
        -----------
        edge: Edge
            Edge to add to graph.
        """
        DirGraph.addedge(self, parent, child)
        DirGraph.addedge(self, child, parent)


class WeightedDirGraph(DirGraph):
    """Weighted directed graph in adjacency list format."""
    # TO DO
    pass


class WeightedGraph(Graph):
    """Weighted undirected graph in adjacency list format."""
    # TO DO
    pass

if __name__ == '__main__':
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

    g.parents('Boston')
