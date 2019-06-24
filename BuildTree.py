#Python wrapper for MediaWiki API
import wikipedia
#import libraries safely, from example
try:
    import pygraphviz
    from networkx.drawing.nx_agraph import graphviz_layout
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import graphviz_layout
    except ImportError:
        raise ImportError("Import Error")

#Tree object to store graph
class Tree:
	def __init__(self):
		import networkx as nx
		self.graph = nx.Graph()
		
#Finds all children for the given node
#Populates origin.children list
def populateLayer(origin, tree):
	#Use wikipedia library to get all links on page
	try:
		linksOnPage = wikipedia.page(origin.getTitle()).links
	except:
		return
	#Iterate over links and add them as children to the origin
	for link in linksOnPage:
		children = []
		if(link != origin.getTitle()):
			origin.addChild(link, children, tree)
def populateTree(origin, depth, tree):
	#TODO: Handle dynamic cases for depth using iteration
	#TODO: Address optimization (if possible) for greater depths
	if(depth >= 1):
		populateLayer(origin, tree)
	if(depth == 2):
		for child in origin.children:
			populateLayer(child, tree) 
	