'''
This module defines classes for storing a basic graph and a basic vertex class
'''
class Vertex:
    '''
    The Vertex object stores info about one vertex of a graph

    Members:
        graph - a graph this vertex belongs to
        supertree - a supertree this vertex belongs to
        id - an id of the vertex
        value - a value of the vertex
    '''
    
    def __init__(self, name : str, value):
        self.value = value
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __str__(self):
        return (self.name + " : " + str(self.value))
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash(self.name)

class Graph:
    '''
    The Graph object stores a graph of vertices (usually Vertex objects).

    Members:
        edges: a multimap that defines which other graphs are connected:  dict<Vertex, list<vertex>>.
        vertices: a set that defines vertices that are in this exact graph
        value: a sum of values of graph's vertices
        id: an integer, unique id
    Methods:
        add: add an edge
        get: get all connected vertices
        merge: merge this graph with another one
    '''

    def __init__(self, id):
        self._edges = {}
        self._vertices = set()
        self.value = None
        self._id = id
    def __hash__(self):
        return self._id

    def __eq__(self, other):
        return self._id == other._id

    def __str__(self):
        return "Graph:\n\tid: " + str(self._id) + "\n\tedges: " + str(self._edges) + "\n"

    def __repr__(self):
        return str(self)

    def add(self, other):
        '''
        Params: addition of an edge in a pair.

        Returns: None

        Result: New edges are added to the graph's multimap variable, vertices set and value are updated

        NOTE: data is not user-generated
        '''
        # edges update
        try:
            if (other[0] != other[1]):
                # edges are 2-way
                l = self._edges.get(other[0], [])
                l.append(other[1])
                self._edges[other[0]] = l

                l = self._edges.get(other[1], [])
                l.append(other[0])
                self._edges[other[1]] = l
            
        except Exception:
            # Should never happen
            # The graph will be incorrect if an exception occurs
            
            raise
        # vertices and value update
        if (other[0] not in self._vertices):
            self._vertices.add(other[0])
            if (self.value == None):
                self.value = other[0].value
            else:
                self.value += other[0].value
        if (other[1] not in self._vertices):
            self._vertices.add(other[1])
            self.value += other[1].value
        return
    
    def merge(self, other): 
        '''
        Params: one extra Graph object

        Result: this graph object will have all vertices of both graphs, 2-way edges
            values will be summed, fullvalue is unchanged
        '''
        if (not isinstance(len, Graph)):
            return

        if (other._vertices is not None):
            self._edges.update(other._edges)
            self._vertices.union(other._vertices)
            self.value += other.value
    
    def get(self, vertex):
        '''
        Params: a vertex

        Returns: a list of all the connections to the vertex in params
        '''
        return self._edges.get(vertex, [])