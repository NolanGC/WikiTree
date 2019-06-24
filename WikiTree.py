'''

WikiTree
Nolan Clement
6/20/19

Program to map all connected wikipedia pages from an origin page.
Generates a wide (many links per page) branching structure.
Goal is to represent in an interesting way.

'''
from BuildTree import populateTree
from Node import Node
from BuildTree import Tree
import matplotlib.pyplot as plt
import networkx as nx
from networkx import draw_networkx_edges
from networkx import draw_networkx_nodes
#pt.set_credentials_file(username='nolangc', api_key='m4P9PEaB1Fk1AFZT1oyH')
#Example origin with random Wikipedia page
children = []
#Example origin with few children
origin = Node("Von Heeringen", children)
#Tree object to store graph
tree = Tree()
plt.figure(figsize=(18,15))
#Fill nodes, depth of 2
populateTree(origin, 2, tree)
#Store position for subsequent function calls
pos = nx.spring_layout(tree.graph)
#Draw edges
nx.draw_networkx_edges(tree.graph, pos, alpha=0.2)
#Draw labels
nx.draw_networkx_labels(tree.graph, pos, font_size=10, alpha=0.5)
#Draw nodes
#Origin is red
nx.draw_networkx_nodes(tree.graph, pos, node_size = 50, alpha=1, nodelist= [origin.getTitle()], node_color="red")
#Make list of firstgen titles to highlight them yellow
firstgen = []
for child in origin.children:
	firstgen.append(child.getTitle())
nx.draw_networkx_nodes(tree.graph, pos, node_size = 30, alpha=1, nodelist= firstgen, node_color="yellow")
#Rest of nodes are green
nx.draw_networkx_nodes(tree.graph, pos, node_size = 10, alpha=0.7, with_labels=True, node_color="green",
	font_size=10)
#Display graph
plt.show()

