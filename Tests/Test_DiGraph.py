import time

from src.DiGraph import DiGraph


def check():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:


    """
    g = DiGraph()  # creates an empty directed graph

    for n in range(100):
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

        g -> Graph: |V|=3 , |E|=5
        {0: 0: score inf, 1: 1: score inf, 2: 2: score inf, 3: 3: score inf}
        {0: 1}
        {0: 1.1, 2: 1.3, 3: 10}
    """
    # g_algo = GraphAlgo(g)
    # print(g_algo.shortest_path(0, 3))


if __name__ == '__main__':
    start_time = time.time()
    check()
    print("--- %s seconds ---" % (time.time() - start_time))