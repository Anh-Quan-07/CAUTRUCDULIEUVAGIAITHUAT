# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:30:33 2021

@author: quann
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_edges_from([('A','B'),('B','C'),('B','D'),('D','C')])


# Specify the edges you want here
red_edges = [('A', 'C')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                        node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()