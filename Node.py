
#Node on the WikiTree
class Node:
	#Nodes contain a page title and children (links)
	def __init__(self, title, children):
		self.title = title
		self.children = children
	#Getter for title
	def getTitle(self):
		return self.title
	#Takes in same arguments as a constructor, adds as child
	def addChild(self, childName, children, tree):
		newChild = Node(childName, children)
		self.children.append(newChild)
		#print("New edge from " + self.getTitle() + " -> " + newChild.getTitle())
		tree.graph.add_edge(self.getTitle(), newChild.getTitle())

