#Python wrapper for MediaWiki API
import wikipedia

#Finds all children for the given node
#Populates origin.children list
def populateLayer(origin):
	#Use wikipedia library to get all links on page
	try:
		linksOnPage = wikipedia.page(origin.getTitle()).links
	except:
		return
	#Iterate over links and add them as children to the origin
	for link in linksOnPage:
		children = []
		origin.addChild(link, children)
def populateTree(origin, depth):
	#TODO: Handle dynamic cases for depth using iteration
	#TODO: Address optimization (if possible) for greater depths
	populateLayer(origin)
	#Example of depth > 1
	if(depth == 2):
		for child in origin.children:
			populateLayer(child)
