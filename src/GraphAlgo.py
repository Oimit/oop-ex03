from typing import List
from src import GraphInterface
from DiGraph import DiGraph
import json
import matplotlib.pyplot as plt
import heapq
import random


class GraphAlgo:

    def __init__(self, graph=None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

        new_graph = DiGraph()

        try:

            with open(file_name, 'r') as json_file:
                data = json.load(json_file)

                # print('data: ', data)

                for node in data['Nodes']:

                    try:
                        pos = node['pos'].split(",")  # -> string = "35.19589389346247,32.10152879327731,0.0"
                        x, y, z = float(pos[0]), float(pos[1]), float(pos[2])

                        new_graph.add_node(node['id'], (x, y, z))

                    except:
                        new_graph.add_node(node['id'])

                for edge in data['Edges']:
                    new_graph.add_edge(edge['src'], edge['dest'], edge['w'])

            self.graph = new_graph
            return True

        except OSError as err:
            print("OS error: {}".format(err))
            return False

        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """

        try:

            nodes = self.graph.get_all_v()

            data = {'Nodes': [], 'Edges': []}

            for node_id in nodes:
                node = self.graph.nodes[node_id]

                data['Nodes'].append({
                    'id': node.id,
                    'pos': node.pos
                })

                ins = node.in_connections
                outs = node.out_connections

                for in_ in ins:
                    data['Edges'].append({
                        'src': in_,
                        'dest': node.id,
                        'w': ins[in_]
                    })

                for out in outs:
                    data['Edges'].append({
                        'src': node.id,
                        'dest': out,
                        'w': outs[out]
                    })

            with open(file_name, 'w') as json_out:
                json.dump(data, json_out)

            return True
        except:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

        if id1 == id2 or id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return float('inf'), []

        distance = {k: float('inf') for k in self.graph.get_all_v()}
        parents = {k: None for k in self.graph.get_all_v()}

        distance[id1] = 0

        pq = [(distance[id1], id1)]  # -> [ (priority = shortest distance, id = node_key) ]

        while pq:

            # pop lowest distance as highest priority
            shortest_d, node_id = heapq.heappop(pq)

            for ni in self.graph.all_out_edges_of_node(node_id):

                alt = distance[node_id] + self.graph.all_out_edges_of_node(node_id)[ni]

                if alt < distance[ni]:

                    distance[ni] = alt
                    parents[ni] = node_id

                    # in java we used COMPERATOR
                    # node1 ? node2
                    # 5  , 10
                    # to use decrease priority in jave we used remove + add
                    heapq.heappush(pq, (alt, ni))

        # get shortest path
        path = self.find_path(parents, id1, id2)

        return distance[id2], path

    def find_path(self, parents, src, dest):
        index = dest
        path = [index] # [1, 2, 3, 4, 5, 6, 7, 8, 9 ..... ]

        while index:
            path.append(parents[index])
            index = parents[index]

            if index == src:
                # INDENT
                return path[::-1]

            # if NONE we have no shortest path
            if index is None:
                return []

    def bfs_util(self, v, nodes, stack):
        q = [v]
        nodes[v].tag = True

        while q:
            indx = q.pop()

            for i in self.graph.all_out_edges_of_node(indx):
                if not nodes[i].tag:
                    nodes[i].tag = True
                    q.append(i)
            stack.append(indx)

    def bfs(self, v, graph, final):
        """

        :param v:
        :param graph:
        :param final:
        :return:
        """
        q = [v]
        final.append(v)
        graph.nodes[v].tag = True

        while q:
            indx = heapq.heappop(q)

            for i in graph.all_out_edges_of_node(indx):

                if not graph.nodes[i].tag:
                    graph.nodes[i].tag = True
                    q.append(i)
                    final.append(i)

        return final

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """

        nodes = self.graph.get_all_v()

        for n in nodes:
            nodes[n].tag = False

        stack = []

        self.bfs_util(id1, nodes, stack)

        # transpose graph
        transpose_graph = self.transpose_graph(self.graph)

        scc_path = []

        self.bfs(id1, transpose_graph, scc_path)

        return list(set(stack).intersection(scc_path))

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """

        nodes = self.graph.get_all_v()
        for n in nodes:
            nodes[n].tag = False

        result = []

        for n in nodes:

            flag = False
            for i in result:
                if n in i: flag = True

            if flag: continue

            for x in nodes:
                nodes[x].tag = False

            stack = []

            self.bfs_util(n, nodes, stack)

            # transpose graph
            transpose_graph = self.transpose_graph(self.graph)

            scc_path = []

            nodes = transpose_graph.get_all_v()

            self.bfs(n, transpose_graph, scc_path)

            result.append(list(set(stack).intersection(scc_path)))

        return result

    def transpose_graph(self, graph):

        new_g = DiGraph()

        for key in graph.get_all_v():
            new_g.add_node(key)

        for key in graph.get_all_v():
            for ni_ki in graph.all_out_edges_of_node(key):
                # connect nodes from id2 to id1
                new_g.add_edge(ni_ki, key, graph.all_out_edges_of_node(key)[ni_ki])

        return new_g

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """

        nodes = self.graph.get_all_v()

        for node in nodes:
            if nodes[node].pos is None:
                x_, y_, z_ = random.uniform(0, self.graph.v_size()), random.randint(0, self.graph.v_size()), 0
                nodes[node].pos = (x_, y_, z_)

        x = []
        y = []
        ids = []

        ax = plt.axes()

        for node in nodes:
            n = nodes[node]
            ids.append(node)
            if n.pos is None:
                x_, y_, z_ = random.uniform(0, self.graph.v_size()), random.randint(0, self.graph.v_size()), 0
            else:
                (x_, y_, z_) = n.pos

            outs = self.graph.all_out_edges_of_node(node)
            for out in outs:

                w = outs[out]
                o_ = nodes[out]

                if o_.pos is None:
                    o_x, o_y, o_z = random.uniform(0, self.graph.v_size()), random.randint(0, self.graph.v_size()), 0
                else:
                    (o_x, o_y, o_z) = o_.pos

                # draw arrow between two points
                # arguments: (x, y, x+dx, y+dx, .....)
                q = ax.quiver(x_, y_, o_x - x_, o_y - y_, angles='xy', scale_units='xy', scale=1)
                # plt.quiverkey(q, x_, y_, 0.5,str(w))

            x.append(x_)
            y.append(y_)

        plt.plot(x, y, 'bo', markersize=10)
        plt.show()


# if __name__ == '__main__':
#     algo = GraphAlgo()
#
#     algo.load_from_json('./data/A0')
