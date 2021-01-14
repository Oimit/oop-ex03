from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def check():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:


    """
    g = DiGraph()  # creates an empty directed graph

    for n in range(5):
        g.add_node(n)

    b = g.add_node(1)
    print("add test (false):" + str(b))  # should return false

    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)

    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)

    g.add_edge(1, 3, 1.9)
    b = g.add_edge(1, 3, 10)
    print("add update weight (false): ", b)

    b = g.remove_edge(1, 3)
    print("remove (true): " + str(b))  # should return true

    b = g.add_edge(1, 3, 10)
    print("add after remove (true): ", b)

    b = g.remove_node(2)
    print("remove node (true): ", b)

    b = g.remove_node(12)
    print("remove node that doesnt exist(false): ", b)

    b = g.add_edge(2, 3, 1.5)
    print("add edge of node that doesnt exist (false): ", b)

    b = g.add_edge(3, 2, 1.5)
    print("add edge of node that doesnt exist (false): ", b)

    b = g.add_edge(3, 3, 1.5)
    print("add edge of node that doesnt exist (false): ", b)

    b = g.add_edge(3, 13, 1.5)
    print("add edge of node that doesnt exist (false): ", b)

    print(g)  # prints the __repr__ (func output)

    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))

    """
        output:

        g -> Graph: |V|=3 , |E|=3
        {0: 0: score inf, 1: 1: score inf, 2: 2: score inf, 3: 3: score inf}
        {0: 1}
        {0: 1.1, 3: 10}
    """
    g_algo = GraphAlgo(g)
    b = g_algo.save_to_json('../data/test_json')
    print("save: ", b)
    # print(g_algo.shortest_path(0, 3))

    # test shortest path

    dist, path = g_algo.shortest_path(0, 3)
    print(f"test shortest path < 0 to 3> -> (2.3, [0,1,2,3]) = {dist}, {path}")

    dist, path = g_algo.shortest_path(0, 50)
    print(f"test shortest path < 0 to 50> -> (inf, []) = {dist}, {path}")

    # dist, path = g_algo.shortest_path(20, 2)
    # print(dist, path)
    # dist, path = g_algo.shortest_path(2, 20)
    # print(dist, path)

    print(f"test SCC from node 0 -> [0, 1] = {g_algo.connected_component(0)}")
    g_ = GraphAlgo()
    g_.load_from_json('../data/A5')

    load_g = g_.get_graph()

    print(load_g)
    print(load_g.get_all_v())  # prints a dict with all the graph's vertices.
    print(load_g.all_in_edges_of_node(1))
    print(load_g.all_out_edges_of_node(1))

    g_.plot_graph()


if __name__ == '__main__':
    check()