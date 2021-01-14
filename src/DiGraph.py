

class DiNode:

    def __init__(self, id, pos=None):

        self.id = id
        self.pos = pos

        self.score = float('inf')

        self.in_connections = {}    # {in_key: weight}
        self.out_connections = {}   # {out_key: weight}

        self.scc = []
        self.tag = False

    def __repr__(self):
        return "id:" + str(self.id) + ", score: " + str(self.score)

    def __str__(self):
        return "id:" + str(self.id) + ", score: " + str(self.score)


class DiGraph:

    def __init__(self):

        self.nodes = {} # {key_of_node: -> node}

        self.mc = 0
        self.edges_size = 0
        self.node_size = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """

        return self.node_size

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edges_size

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        # in_ = self.nodes[id1].in_connections
        return self.nodes.get(id1).in_connections

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        return self.nodes.get(id1).out_connections

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def hasEdge(self, id1, id2) -> bool:
        """
        this function checks for edge between id1 and id2
        :param id1: key of node1
        :param id2: key of node2
        :return: true iff edge exist between id1->id2
        """
        out = self.nodes.get(id1).out_connections
        return id2 in out

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

        if id1 in self.nodes and id2 in self.nodes:

            node1 = self.nodes.get(id1)
            node2 = self.nodes.get(id2)

            if weight > 0:
                if id1 != id2:
                    if not self.hasEdge(id1, id2): #HAS EDGE

                        # id2 into id1 -> if id2 is not in id1
                        # id1 into id2 -> if id1 is not in id2
                        node1.out_connections[id2] = weight
                        node2.in_connections[id1] = weight

                        self.edges_size += 1
                        self.mc += 1

                        return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """

        if node_id not in self.nodes:

            self.nodes[node_id] = DiNode(node_id, pos)
            self.node_size += 1

            return True

        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """

        if node_id in self.nodes:

            node = self.nodes.get(node_id)

            for i_ in node.in_connections: # case 1: delete all in to node_id

                out_node = self.nodes[i_]
                outs_ = out_node.out_connections

                del outs_[node_id]
                self.edges_size -= 1

            outs = node.out_connections

            for out in outs: # case 2: delete all node_id in out nodes
                out_node = self.nodes[out]
                del out_node.in_connections[node_id]

            self.node_size -= 1
            self.edges_size -= len(outs)     # case 3: delete all out edges
            del self.nodes[node_id]     # case 3: delete

            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """

        if self.hasEdge(node_id1, node_id2):

            node1 = self.nodes.get(node_id1)
            node2 = self.nodes.get(node_id2)

            del node1.out_connections[node_id2]
            del node2.in_connections[node_id1]

            self.edges_size -= 1
            return True

        return False

    def __repr__(self):
        return "|V|=" + str(self.node_size) + ", |E|=" + str(self.edges_size)

    def __str__(self):
        return "|V|=" + str(self.node_size) + ", |E|=" + str(self.edges_size)
