import networkx as nx

from utils.api import get_input

inp = get_input(25)
edges = []
for line in inp.splitlines():
    first, seconds = line.split(": ")
    seconds = seconds.split()
    for second in seconds:
        edges.append((first, second))
G = nx.Graph()
G.add_edges_from(edges)
G.remove_edges_from(nx.minimum_edge_cut(G))
connected_components = list(nx.connected_components(G))
print(len(connected_components[0]) * len(connected_components[1]))
