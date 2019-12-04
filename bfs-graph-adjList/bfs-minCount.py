from graphProgram import Vertex, Graph
import collections
import random as r
import time as t

# bfs returns min hop count + Path
def bfs(G, s, t):

    if isinstance(s, Vertex) and isinstance(t, Vertex):
        pass
    elif isinstance(s, str) and isinstance(t, str):
        s = Vertex(s)
        t = Vertex(t)

    V = G.getVertices()
    hop = 0

    for vertex in V:
        vertex.setColor('white')
        vertex.setDistance(float('inf'))
        vertex.setParent(None)
        # Get the target s from the Graph and map it to x
        if(vertex == s):
            x = vertex
            x.setColor('gray')
            x.setDistance(0)
            x.setParent(None)
        # check if all inits are correct
        # print(vertex.getName(), ' : ', vertex.getColor())

    # use of deque to ensure O(1) for pop
    queue = collections.deque([x])

    while queue:
        u = queue.popleft()
        for v in u.getNeighbors():
            if v.getColor() == 'white':
                v.setColor('gray')
                v.setDistance(u.getDistance() + 1)
                v.setParent(u)
                if(v==t):
                    hop = str(v.getDistance())
                    p = v
                    hop += ' and Path : ' + v.getName()
                    while p.getParent() != None:
                        p = p.getParent()
                        hop += '<-' + p.getName()
                queue.append(v)
            u.setColor('black')

    return hop

# Random graph generator - both directed/undirected
def randGraph(vertices, edges, directed=False):

    g = Graph(directed)

    for i in range(1, vertices+1):
        v = 'N' + str(i)
        g.addNode(Vertex(v))

    for i in range(edges):
        randomV1 = r.randint(1,vertices)
        u = 'N' + str(randomV1)
        randomV2 = r.randint(1, vertices)
        v = 'N' + str(randomV2)
        g.addEdge(Vertex(u),Vertex(v))

    return g


def userResult(n):

    output = open('output_minhop.txt', 'w+')
    output.write('\n\nNodes\tEdges\tTime Taken\n')


    while(n!=0):
        print('\n\nGenerate random graph + find min hop between 2 Nodes')
        input_node = input('Enter number of nodes : ')
        input_edges = input('Enter number of edges : ')
        input_directed = input('Enter D/U for directed/undirected graph property : ')
        if len(input_directed) == 1:
            input_directed = True if input_directed == 'D' else False
            g = randGraph(int(input_node), int(input_edges), input_directed)
        else:
            print('Invalid input for Directed\nProceeding with an undirected Graph')
            g = randGraph(int(input_node), int(input_edges))

        g.printGraph()
        input_s = input('Enter start node : ')
        input_t = input('Enter target node : ')
        if len(input_s) <= len(input_node) + 1 and len(input_t) <= len(input_node)+1:
            start = t.perf_counter_ns()
            hop = bfs(g, input_s, input_t)
            end = t.perf_counter_ns()

            print('Distance from {} to {} is {}'.format(input_s,input_t,hop))
        else:
            print('Invalid Input!')

        # Write to file operations
        text =  str(input_node) + '\t' + str(input_edges) + '\t' + str(end-start) + ' ns\n'
        output.write(text)
        text = 'Result : Distance from node {} to node {} is {}'.format(input_s,input_t,hop) + '\n\n'
        output.write(text)

        del g
        
        n-= 1

    output.close()

user = input('Enter number of minhop runs to run : ')
userResult(int(user))