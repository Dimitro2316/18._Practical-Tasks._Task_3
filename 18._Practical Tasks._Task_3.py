import networkx as nx


def is_tree(graph):
    num_edges = graph.number_of_edges()
    num_nodes = graph.number_of_nodes()

    if num_edges != num_nodes - 1:
        return False

    return nx.is_connected(graph)


tree_graph = nx.Graph()
tree_edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
tree_graph.add_edges_from(tree_edges)

print("Граф является деревом:", is_tree(tree_graph))


not_tree_graph = nx.Graph()
not_tree_edges = [(1, 2), (2, 3), (3, 1)]
not_tree_graph.add_edges_from(not_tree_edges)

print("Граф является деревом:", is_tree(not_tree_graph))


disconnected_graph = nx.Graph()
disconnected_edges = [(1, 2), (3, 4)]
disconnected_graph.add_edges_from(disconnected_edges)

print("Граф является деревом:", is_tree(disconnected_graph))








