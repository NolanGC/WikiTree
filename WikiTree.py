'''

WikiTree
Nolan Clement
6/20/19

Program to map all connected wikipedia pages from an origin page.
Generates a wide (many links per page) branching structure.
Goal is to represent in an interesting way.

'''

import wikipedia
from BuildTree import populateTree
from Node import Node
#Example origin with random Wikipedia page
children = []
origin = Node("Habba Khatoon", children)
#Tree starting at "Habba Khatoon," depth of 2
populateTree(origin, 2)
f = open("tree.xml", "wb+")
origin.listChildren(f)
for child in origin.children:
	child.listChildren(f); 


