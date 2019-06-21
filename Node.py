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
	def addChild(self, childName, children):
		newChild = Node(childName, children)
		self.children.append(newChild)
	#Writes wiki tree to xml file, placefolder for testing
	def listChildren(self, f):
		output = self.getTitle() + "'s children: "
		for child in self.children:
			output += child.getTitle() + ","
		output += "\n\n"
		f.write(output.encode())
