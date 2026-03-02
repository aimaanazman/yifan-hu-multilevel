import networkx as nx
from yifan_hu import yifan_hu_layout
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(100, 0.05)

pos = yifan_hu_layout(G)

nx.draw(G, pos, node_size=10)
plt.show()
