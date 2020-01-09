"""Graph processing algorithms."""

from structures.graph import Path, DirGraph


class DirGraphProcess(DirGraph):
    """Graph processing algorithms for directed graph class."""

    def dfs_rec_shortpath(self, start, end, path=Path([]), shortpath=None):
        """Recursive depth-first shortest path between two vertices.

        Parameters
        ----------
        start: Vertex
            Vertex to start search at
        end: Vertex
            Vertex to end at
        path: Path, default empty
            Current path
        shortpath: Path, default None
            short path so far


        Returns
        -------
        shortpath: Path
            Shortest path from start to end.
        """
        # check start and end are in graph
        if start not in self.vertices:
            raise ValueError('Start vertex not in graph')
        if end not in self.vertices:
            raise ValueError('End vertex not in graph')
        # add starting vertex to path
        path = path + Path([start])
        # if we've reached the end return path
        if start == end:
            return path
        # for each child of start vertex
        for vertex in self.children(start):
            # if vertex hasn't been visted
            if vertex not in path:
                # if path is shorter than shortpath
                if shortpath is None or len(path) < len(shortpath):
                    # get short path from new vertex to end
                    newpath = self.dfs_rec_shortpath(vertex, end, path,
                                                     shortpath)
                    # if short path is found its <= length of shortpath
                    if newpath is not None:
                        shortpath = newpath
        return shortpath

    def dfs_it_shortpath(self, start, end):
        """Iterative depth-first shortest path between two vertices.

        Parameters
        ----------
        start: Vertex
            Vertex to start search at
        end: Vertex
            Vertex to end at

        Returns
        -------
        shortpath: Path
            Shortest path from start to end.
        """
        pathqueue = [Path([start])]
        shortpath = None
        while pathqueue:
            tmppath = pathqueue.pop()
            lastvertex = tmppath.vertices[-1]
            if lastvertex == end and shortpath is None:
                shortpath = tmppath
            elif lastvertex == end and len(tmppath) < len(shortpath):
                shortpath = tmppath
            for nextvertex in self.children(lastvertex):
                if nextvertex not in tmppath:
                    newpath = tmppath + Path([nextvertex])
                    pathqueue.append(newpath)
        return shortpath

    def bfs_it_shortpath(self, start, end):
        """Iterative breadth-first shortest path between two vertices.

        Parameters
        ----------
        start: Vertex
            Vertex to start search at
        end: Vertex
            Vertex to end at
        path: Path, default empty
            Current path

        Returns
        -------
        shortpath: Path
            Shortest path from start to end.
        """
        pathqueue = [Path([start])]
        while pathqueue:
            # Get and remove oldest element in pathQueue

            tmppath = pathqueue.pop(0)
            lastvertex = tmppath.vertices[-1]
            if lastvertex == end:
                return tmppath
            for nextvertex in self.children(lastvertex):
                if nextvertex not in tmppath:
                    newpath = tmppath + Path([nextvertex])
                    pathqueue.append(newpath)
        return None

    def dfs_rec_traversal(self, start, reachable=set()):
        """Recursive depth-first traversal from start.

        Parameters
        ----------
        start: Vertex
            Vertex to start search at
        reachable: set of Vertexs, default empty
            set of vertices reachable from start vertex.

        Returns
        -------
        reachable: set of Vertexs
            set of vertices reachable from start vertex
        """
        reachable.add(start)
        for vertex in self.children(start):
            if vertex not in reachable:
                reachable = self.dfs_rec_traversal(vertex, reachable)
        return reachable

    def dfs_it_traversal(self, start, reachable=set()):
        """Recursive depth-first traversal from start.

        Parameters
        ----------
        start: Vertex
            Vertex to start search at
        reachable: set of Vertexs, default empty
            set of vertices reachable from start vertex.

        Returns
        -------
        reachable: set of Vertexs
            set of vertices reachable from start vertex
        """
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in reachable:
                reachable.add(vertex)
                for child in self.children(vertex):
                    stack += [child]
        return reachable

    def bfs_it_traversal(self, start):
        """Iterative breadth-first search traversal from start.

        Parameters
        ----------
        start: Vertex
            Vertex to start search at

        Returns
        -------
        traversal: list of Vertexs
            List of vertices reachable from start vertex.
        """
        pass
