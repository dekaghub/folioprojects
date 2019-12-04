# function to find & return single element from list
def listObject(A, x):
    for i in A:
        if i == x:
            return i

# Vertex to add into graphs (as nodes) and to store information of the graph
class Vertex():

    def __init__(self, n):
        self.color = 'none'
        self.name = n
        self.distance = 0
        self.parent = None
        self.neighbors = list()

    # Override equality operator to get correct comparisons
    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.name == other.name
        return False

    def addNeighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)

    def getName(self):
        return self.name

    def getNeighbors(self):
        return self.neighbors

    def getNeighborNames(self):
        temp = []
        for i in self.neighbors:
            temp.append(i.getName())
        return temp

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.distance

    def getParent(self):
        return self.parent

    def setColor(self, x):
        self.color = x

    def setDistance(self, x):
        self.distance = x

    def setParent(self, x):
        self.parent = x

# Graph with self-descriptive everything
class Graph():

    vertices = []

    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed
        self.vertices = []

    # Add single node
    def addNode(self, node):
        if isinstance(node, Vertex) and node not in self.vertices:
            self.vertices.append(node)
            self.adj_list[node.getName()] = node
    
    # Add list of nodes
    def addNodes(self, nodes):
        for node in nodes:
            if isinstance(node, Vertex) and node not in self.vertices:
                self.vertices.append(node)
                self.adj_list[node.getName()] = node

    def addEdge(self, u, v):
        if isinstance(u, Vertex) and isinstance(v, Vertex) and u in self.vertices and v in self.vertices:
            if u.getName() != v.getName():
                for key, value in self.adj_list.items():
                    if key == u.getName():
                        p = listObject(self.vertices, v)
                        value.addNeighbor(p)
                        # check if edge is added correctly
                        # print('current ', key, '  neighbor add', v.getName())
                        # print('value : ', value.getName())
                    if self.directed:
                        if key == v.getName():
                            p = listObject(self.vertices, u)
                            value.addNeighbor(p)
    
    def printGraph(self):
            for key, value in list(self.adj_list.items()):
                print(key, ' - ', str(value.getNeighborNames()))

    def getVertices(self):
        return self.vertices
