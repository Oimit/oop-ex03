# oop-ex03


Background: This next file will explain the purpose of this assignment. 
In this assignment we build a graph in Python language, which we makes some algorithems on it.
We also comparing the graph we created, with the graph we created in Java at the last assignment and,
we also compating with the Python library "NetworkX" and we comparing few things:
1. Load json files.
2. ShortestPath.
3. Connected Components.

 The assignment has 3 parts:

First part: implements a graph and node.
Second part: implements algorithems on a graph.
Third part: comparing this assignment with the library of NetworkX and with java assignment.

______________________________________________

First part: 

In this part we created a graph by building another class of Node.
each Node has a key and position. -> If position is nongiven, random position will be set.
Using the DiNode class will creates a graph with simple functions such as: DeleteNode, AddNode, AddEdge and Sizes.

______________________________________________

Second Part:

In this part we created more complicated algorithems on the graph using the implemintation of DiGraph.
In this class we have the algorithems: ShortestPath with Dijakstra algorithem.
 SCC (Strongly Connected Component) with Kosaraju's algorithem which uses BFS on the original graph, than, transpose the edges
of the graph, and than we used the BFS algo again. More info here: https://www.programiz.com/dsa/strongly-connected-components .
We also have load & save functions to read Json files.

______________________________________________

Third part:

In this part we needed to compare our project in Python to the project in Java we did on oop Ex2, and also with
the library of NetworkX.

With the given graphs we got from the Json's, we compared the: SCC, ShortestPath, Load and SCC Single.
Our conclusion from the comparisment are:
LoadTime: Python has the highest time, and NetworkX and Java were almost equals.
SCC: Java was the fastest, and Python was slowest.
SCC Single: Python won Java on time while NetworkX dont have a function for a SCC Single.
ShortestPath: Python was the slowest by far. NetworkX was almost 0 on most of the graphes,
and java was in the middle.


