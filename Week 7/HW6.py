## HW6
## Due Wed March 29 at 11:59 PM
## GraphSpace: www.reed.edu/biology/ritz/graphspace
## Username: compbio@reed.edu 
## Password: compbio

##Notes:
#DB indicates lines used for debugging/info during runtime
#Whoa, semicolons can combine lines!!  Discovery!!!

##Citations:
#generate_kmers is a cut-down version of frequentKmers from HW4
#list(dictionary.keys()) is from https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python


##Questions:
#How do you change less direct node attributes in GraphSpace?  Particularly things like 'content'.
#How do you create variables in a for loop?  e.g. a loop makes variables bcd1, then bcd2, then bcd3, while automated?

################################
## Nick Egan
## Estimate time spent: 2 + 3 + 1
################################

import HW6_utils ## import utility functions

def main():
	dna_for_handin = 'TAATGCCATGGGATGTT'
	dna = 'abcdbcde'
	k=3
	
	kmerList = generate_kmers(dna, k)
	de_bruijn(kmerList)
	overlap(kmerList)
	
	## an example graph post
	##test_graphspace(['a','b','c','d'],'Your-Name')

	return

def generate_kmers(genome, lenKmer):
	##Inputs: a string genome and an integer lenKmer
	##Outputs: a list of k-mers including duplicates
	##Borrowed and cut-down version from HW4
	stringCutter = ""
	kmerList = []
	
	for i in range(len(genome)):
		stringCutter = genome[i:i+lenKmer]
		if len(stringCutter) < lenKmer:
			#print ("Short kmer detected.")  #DB
			break
		kmerList.append(stringCutter)
		#print("The found patterns were: ", kmerList)    #DB
		#print("For round ", i," the stringCutter is reading: ", stringCutter)   #DB
	
	return kmerList
	
def de_bruijn(kmerList):
	##Inputs: a list of k-mers
	##Outputs: A list of edges, where each edge is a list of two strings
	##where one is the first k-1 letters, the other is the last k-1 letters of the kmer
	edgeList = []
	prefix = []
	suffix = []
	fixer = []  #holds prefix and suffix together in a temporary array
	stringCutter = ""
	
	for i in range(len(kmerList)):
		stringCutter = kmerList[i]
		prefix.append(stringCutter[0:len(stringCutter)-1])  #Generates a list of the first k-1 length nodes
		suffix.append(stringCutter[1:len(stringCutter)])  #Generates a list of the last k-1 length nodes
		#print("The prefixes are: ", prefix)   #DB
		#print("The suffixes are: ", suffix)  #DB
		
		fixer = [prefix[i], suffix[i]]
		edgeList.append(fixer)
		fixer = []
	
	print("The edgeList is: ", edgeList)
	
	node_attrs = basic_node_attributes(edgeList) # some node attributes
	HW6_utils.postBio131Graph(edgeList,node_attrs,'Nick-Egan-deBruijn')
	
	return edgeList
	
def overlap(kmerList):
	##Inputs: A list of k-mers
	##Outputs: a list of edges, where each edge is a list of two strings.
	##In an overlap graph, the nodes are k-mers, and the edges are the prefixes/suffixes

	edgeList = []
	prefix = []
	suffix = []
	fixer = []   #holds prefix and suffix together in a temporary array
	stringCutter = ""
	
	##For cutting out repetitive edges.
	trackingDict = {}

	#Initializes the dictionary
	for i in range(len(kmerList)):
		trackingDict[kmerList[i]] = 0
	#Uses the dictionary as a counter for each node.	
	for i in range(len(kmerList)):
		trackingDict[kmerList[i]] = trackingDict[kmerList[i]] + 1
	#Pulls the list of keys from the dictionary - making every kmer non-repetitive.
	newkmerList = list(trackingDict.keys())
	#print(trackingDict)   #DB
	
	##If duplicating the nodes:
	#Could scan through trackingDict and see which keys have a value > 1
	#Those ones would be have more elements in the newkmerList
	#How do you create variables in a for loop?  e.g. each loop makes bcd1, then bcd2, then bcd3, while automated?
	
	#Creates the lits of edges from the unique-edges-list made by the dictionary as newkmerList
	for i in range(len(newkmerList)):
		for j in range(len(newkmerList)):
			stringCutter = kmerList[i]
			suffix = stringCutter[0:len(stringCutter)-1]
			stringCutter = kmerList[j]
			prefix = stringCutter[1:len(stringCutter)]
			if suffix == prefix:
				edge = [newkmerList[j],newkmerList[i]]
				edgeList.append(edge)
			
	#print(kmerList)  #DB

	node_attrs = basic_node_attributes(edgeList) # some node attributes
	#node_attrs[node1]['content'] = trackingDict
	#node_attrs[node2]['content'] = trackingDict  
	##Unsure how to change node attributes.
	HW6_utils.postBio131Graph(edgeList,node_attrs,'Nick-Egan-Overlap')
	
	print("The final edgeList is: ", edgeList)
	
	return edgeList
	
def test_graphspace(listOfStrings,your_name):
	## Simple test function
	## takes a list of strings and adds edges between them.
	edge_list = []
	for i in range(len(listOfStrings)-1):
		## node 1 is the ith k-mer, node 2 is the (i+1)st k-mer
		node1 = listOfStrings[i]
		node2 = listOfStrings[i+1]
		## append the edge [node1,node2] to the list.
		## note that you need to append a LIST of a list
		edge_list = edge_list + [[node1,node2]]
	print('test edge list:',edge_list)

	## get basic node attribtues (background color only)
	node_attrs = basic_node_attributes(edge_list)

	## post graph to GraphSpace.
	HW6_utils.postBio131Graph(edge_list,node_attrs,your_name+'-test')
	print('Done!')
	return

def basic_node_attributes(edge_list):
	## build dictionary of node colors only.
	node_attrs = {}
	for e in edge_list:
		node1 = e[0]  # node1 = first element of edge e
		node2 = e[1]  # node2 = second element of edge e 
		## if node1 isn't in node_attrs dictionary, add background color.
		if node1 not in node_attrs:
			node_attrs[node1] = {}
			node_attrs[node1]['background_color'] = '#9999FF'

		## if node2 isn't in node_attrs dictionary, add background color.
		if node2 not in node_attrs:
			node_attrs[node2] = {}
			node_attrs[node2]['background_color'] = '#9999FF'
	return node_attrs

if __name__ == '__main__':
	main()