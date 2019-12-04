# Graph - Breadth First Search (BFS)

The bfs algorithm requires a graph object and two nodes from the graph to calculate the distance between the two nodes.

There is a graph class and a vertex class to generate random graphs of any size. The graphs can be generated either directed or undirected.

The bfs algorithm here is the python implementation of [Intro. to Algorithms, 3rd Ed, 595](https://mitpress.mit.edu/books/introduction-algorithms-third-edition).

## Challenges

Since this is a Python implementation, the graph class and the bfs algorithm needed to be designed in a way to work with Python's object notation i.e. everything in Python is an object.

To ensure that the running time of BFS is mainly dependent on only the size of input, I used deque (queue) from the library collections where deque.popleft() takes O(1) constant time.

# Files in the project directory

[graphProgram.py](./graphProgram.py) : Contains Graph, Vertex class

[bfs-minCount.py](./bfs-minCount.py) : Driver program that contains bfs code

[output_minhop.txt](./output_minhop.txt) : Output from driver program

# Execution

Recommended **Python 3.8**

    python bfs-minCount.py

First enter the number of times you would like to generate random graphs as well as the BFS (minhop) algorithm.

Then enter the number of nodes and the number of edges.

The third prompt determines if you want the graph to be generated with directed edges i.e. nodes that only point to other nodes or undirected edges i.e. nodes that can point to other nodes or its parent as well.

After that the graph will be generated and you'll be prompted to enter the start node and the target node.

Enter the node name NX where X is the node number.
This can be modified in the function randGraph(x,y).

To view the output file, use the following command.

    cat output_minhop.txt

You can comment out or edit userResult() to customize.
