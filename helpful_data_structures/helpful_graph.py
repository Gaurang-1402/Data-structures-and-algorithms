class Graph:
    """Representation of a simple graph using an adjacency map."""

    class Vertex:
        """Lightweight vertex structure for a graph."""

        def __init__(self, x):
            """Do not call constructor directly. Use Graph sinsert vertex(x)."""
            self.element = x

        def element(self):
            """Return element associated with this vertex"""
            return self.element

        def __hash__(self):
            return hash(id(self)) # will allow vertex to e a map/set key

    class Edge:
        """Lightweight edge structure for a graph."""

        def __init__(self, u, v, x):
            """Do not call constructor directly. Use Graph sinsert edge(u,v,x)."""
            self.origin = u
            self.destination = v
            self.element = x


        def endpoints(self):
            """ Return the vertex that is opposite v on this edge."""
            return (self.origin, self.destination)

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            return self.destination if v is self.origin else self.origin

        def element(self):
            """Return the element associated with this edge"""
            return self.element

        def __hash__(self):
            return hash((self.origin, self.destination))

    def __init__(self, directed = False):

        """Create an empty graph (undirected, by default).
        Graph is directed if optional paramter is set to True.
        """

        self.outgoing = {}

        # only create second map for directed graph; use alias for undirected
        self.incoming = {} if directed else self.outgoing

    def is_directed(self):

        """Return True if this is a directed graph; False if undirected.
        Property is based on the original declaration of the graph, not its contents.
        """

        return self.incoming is not self.outgoing # directed if maps are distinct

    def vertex_count(self):

        """Return the number of vertices in the graph.””” return len(self. outgoing)"""

        return len(self.outgoing)


    def vertices(self):
        """Return an iteration of all vertices of the graph."""

        return self.outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""

        total = sum(len(self.outgoing[v]) for v in self.outgoing)

        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges of the graph."""

        result = set()

        for secondary_map in self.outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        return self.outgoing[u].get(v) # returns None if v is not adjacent

    def degree(self, v, outgoing=True):
        """"Return number of (outgoing) edges incident to vertex
        v in the graph. If graph is directed, optional parameter used to
        count incoming edges.
        """


        adj = self.outgoing if outgoing else self.incoming

        return len(adj[v])

    def incident_edges(self, v, outgoing = True):
        """Return all (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to request incoming edges.
        """

        adj = self.outgoing if outgoing else self.incoming

        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x = None):
        """Insert and return a new Vertex with element x."""

        v = self.Vertex(x)
        self.outgoing[v] = {}
        if self.is_directed():
            self.incoming[v] = {}
        return v

    def insert_edge(self, u, v, x = None):

        """Insert and return a new Edge from u to v with auxiliary element x."""

        e = self.Edge(u, v, x)
        self.outgoing[u][v] = e
        self.incoming[v][u] = e

def DFS(g, u, discovered):
    """
    Perform FS of the undiscovered portion of Graph g starting at Vertex u.

    discovered is a dictionary mapping each vertex to the edge that was used to discover it during the DFS. (u should be ”discovered” prior to the call.)

    Newly discovered vertices will be added to the dictionary as a result.


    FANTASTIC EXPLANATORY VIDEO --> https://www.youtube.com/watch?v=pcKY4hjDrxk&t=847s

    """

    # for every outgoing edge from u # v is an unvisited vertex
    # e is the tree edge that discovered v
    # recursively explore from v

    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)










