## Final Project - Utilizing GraphSpace to Showcase Synteny Transformations

## Notes
#Have not tested with a real DNA sequence yet - just increasingly large test sequences.  Too worried about runtime!  It gets wild long!
#Haven't tested, but most likely does not yet work if there is more than one ideal sequence of flips that is the same # of flips as another ideal set of flips.

## Citations
#singleFlipper modified from HW3's Reverse Complement function
#GlobalAlignment and initialize_table modified from HW7.py
#sorted() function from https://developers.google.com/edu/python/sorting
#Recursion suggestion and help on returning a multi-entried dictionary from Mina!
#generator expressions from https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
#^ not in final product - it got messy
#GraphSpace function from HW6

## Questions

####################################################
## Nick Egan
## BIO 131 Intro to Computational Biology
## 5/9/2017
## Time Spent: 3 + 8 + 2 + 3 + 3 + 3 + 2 = 24 hours!
####################################################

import graphspace_utils ## import utility functions for GraphSpace

def main():
	
	## Part 1: Synteny block consruction
	''' 
	In this part, we are taking strings, flipping them in all possible ways, then performing global alignment comparison
	of all possible flips with the string it is trying to match.  The best scored sequence of flips will be retained, and
	will move onto the graphing in Part 2.
	'''
	
	# tests1 = "AAATCGATCG"
	# tests2 = "AAGCTAGCAT"   #2 strings, should require 3 flips to reach #update: program found an even more optimized route in two flips! this program smarter than me lol #DB
	
	tests1 = "AAATCGATCGACGAAATCTCGATAATCGATCGACGAAATCTCGATCGATCGACGAAATCGATTCGATCCGATCGACGAAATCGATTCGATCG"
	tests2 = "AAATCGATCGACGAAATCTCGATCGATCGACGAAATCGATTCGATCAGCAAGCCGATAGCATAATCGCTAGTCCGAGATCGATCATTAGCAT"   #big ol' strings to make sure an output is produced.  Has perfect conservancy. #DB
	#^ above test strings have a runtime of >180 minutes.
	
	s1 = tests1
	s2 = tests2
	
	historyFlip = {}  #Maintains history of flips.
	tempHolder = s1
	howManyRecursions = 0 #Keeps track of # of recursive loops
	bestScore = False
	
	#tempHolder, historyFlip[tempHolder] = 
	historyFlip = massFlipper(tempHolder, s2, historyFlip, False)
	#Each entry in historyFlip/finalDict is coded this way:
	#post-flip sequence: pre-flip sequence, flipped section of sequence, GlobalAlignment score compared with the ultimate string
	
	while howManyRecursions < 1 and bestScore == False: #How many recursive loops are allowed to occur before program cancels and creates output.  Cancels early if exact match is produced.
		historyFlip = massFlipper(tempHolder, s2, historyFlip, False)
		howManyRecursions = howManyRecursions + 1
		bestScore = bestPossibleScore(historyFlip, s2)

	#print(historyFlip)  #DB
	
	## Part 2: Backtracking
	'''
	In this part, we are attempting to reconstruct the flipping path of the best scored series of flips,
	and then graphically show the path.
	'''
	
	historyFlip, sequenceList, flipList = flipOptimization(historyFlip, s1)
	print("The steps of the highest scoring flipped sequence is: ", historyFlip)
	print("The chosen list of sequences, from result to start is: ", sequenceList)
	print("The list of transformations, towards result from start is: ", flipList)
	
	#node_attrs = basic_node_attributes(edgeList) # some node attributes
	#node_attrs[node1]['content'] = trackingDict
	#node_attrs[node2]['content'] = trackingDict  
	##Unsure how to change node attributes.
	#graphspace_utils.postBio131Graph(edgeList,node_attrs,'Nick-Egan-Overlap')
	
	#test_graphspace(sequenceList, "Nick_Egan")
	
	return
	
def massFlipper(s1, s2, finalDict, recurseCheck):
	##Finds matches between strings, so that they can be tested for synteny.
	#Input: Two strings
	#Output: Array that indicates the best scoring sequence of flips
	
	sequencesToExamine = sorted(finalDict.keys())
	if len(sequencesToExamine) > 0 and recurseCheck == False:  #After the first run through, this activates! byewww!  It runs through all the post-flip strings, and produces flips/alignments for them as well.
		#print("!!ENTERING RECURSION!!")  #DB
		recurseCheck = True
		for i in range(len(sequencesToExamine)):
			finalDict = massFlipper(sequencesToExamine[i], s2, finalDict, True)
		recurseCheck = False
		return finalDict
	
	whatWillFlip = []  #The section of the string to be flipped.
	tempFlipHolder = ""  #Holds a string beind constructed while a flip is being built
	allFlipHolder = []   #Holds all possible flips during each section of the function
	sequenceFlipRecorder = {} #Dict that holds what things are flipped for each sequence.
	indexFlip = 0 #Maintains position for sequenceFlipRecorder
	bestFlipHolder = ""  #Holds the highest scoring flip during each section of the function
	#finalDict = {}  #Dictionary of the highest scoring sequences with flips.
	
	#print("String 1 is: ", s1)  #DB
	#print("String 2 is: ", s2)  #DB
		
	for i in range(len(s1)):
		for n in range(i, len(s1)):
			whatWillFlip = s1[i:n+1]  #The section of the string to be flipped
			
			tempFlipHolder = singleFlipper(whatWillFlip)  #The flipped section of the string
			
			toBeAdded = s1[0:i] + tempFlipHolder + s1[n+1:len(s1)] #The full string w/ flipped sections
			
			allFlipHolder.append(toBeAdded) #Holds all post-flip strings in this run.
			tempList = [whatWillFlip]   #Adds section being flipped to a list, so that more can be added in dictionary form.
			sequenceFlipRecorder[toBeAdded] = tempList  #Dictionary that holds the sections that are being flipped

	#print("All possible flip strings are: ", allFlipHolder)  #DB #Open this if you wanna see the program get wild!
	print(sequenceFlipRecorder)   #DB for checking dictionary  #DB  #Open this if you wanna see the program get wild!
	
	##Determining highest scored flip
	scoreKeeper = []
	highestScore = ""
	
	for i in range(len(allFlipHolder)):
		scoreKeeper.append(GlobalAlignment(s2,allFlipHolder[i], 0, 1, 1)) #Generates scores for each flipped sequence produced
	maxVal = max(scoreKeeper)  #Takes the highest score of all the flip sequences
	for i in range(len(allFlipHolder)):  #For all flipped sequences...
		if scoreKeeper[i] == maxVal:   #If it's a sequence with the highest score...
			#Place into the dictionary that will be returned at the end.
			highestScore = allFlipHolder[i]
			
			sequenceFlipRecorder[highestScore].append(scoreKeeper[i])
			finalDict[highestScore] = sequenceFlipRecorder[highestScore]
			finalDict[highestScore].insert(0, s1)
			if len(finalDict[highestScore]) > 3:  #In case there are existing values for an entry, it removes the ones being added in. #?Explore possible room for error?
				finalDict[highestScore].pop();finalDict[highestScore].pop();finalDict[highestScore].pop();
		#print(scoreKeeper)
		highestScore = [allFlipHolder[i], scoreKeeper[i]]
	#print(highestScore) #DB
	#print(sequenceFlipRecorder) #DB
	#print(finalDict)  #DB
	return finalDict

def GlobalAlignment(string1, string2, indel, matchscore, mismatchpenalty):
	#Input: strings s1 and s2, and three integers indel, matchscore, and mismatchpenalty
	#Function: scores alignment of strings based on indels, matching, and mismatches.
	#Output: score of the optimal global alignment and the alignment itself,
	
	#print("\nStart of GlobalAlignment.\n")   #DB
	
	
	GlobalTable = []
	bestOption = 0
	GlobalHolder = []
	
	#Creates a blank table in the lengths of strings + 1
	GlobalTable = initialize_table(len(string2)+1,len(string1)+1)
	GlobalBacktrack = initialize_table(len(string2)+1,len(string1)+1)

	
	for i in range(len(string1)+1):
		for j in range(len(string2)+1):
			GlobalHolder = []
			directionality = []
			if i > 0:
				GlobalHolder.append(GlobalTable[i-1][j] - indel)
				directionality.append("s")
			if j > 0:
				GlobalHolder.append(GlobalTable[i][j-1] - indel)
				directionality.append("e")

			if i > 0 and j > 0:
				if string1[i-1] == string2[j-1]:
					GlobalHolder.append(GlobalTable[i-1][j-1] + matchscore)
					directionality.append("d")
				else:
					GlobalHolder.append(GlobalTable[i][j] - mismatchpenalty)
					directionality.append("d")
				
			#print(i,j,GlobalHolder,directionality)     #DB    see possible directions out of a node and their respective # of points
			if i != 0 and j != 0:
				GlobalTable[i][j] = max(GlobalHolder)
			if i == 0 and j == 0:
				GlobalBacktrack[i][j] = "*"
			elif max(GlobalHolder) == GlobalHolder[0]:
				GlobalBacktrack[i][j] = directionality[0]
			elif max(GlobalHolder) == GlobalHolder[1]:
				GlobalBacktrack[i][j] = directionality[1]
			elif max(GlobalHolder) == GlobalHolder[2]:
				GlobalBacktrack[i][j] = directionality[2]
	
	longest = max(map(max, GlobalTable))  #DB   Finds the largest value of all spots in the table.
	#print(longest)  #DB  Seeing what the highest score in the table is/LCS
	
	#printTable(GlobalTable, string1, string2)
	#printTable(GlobalBacktrack, string1, string2)
	
	return longest

def initialize_table(ncols, nrows):
	##Input: two integers, the number of rows and columns
	##Output: nrows by ncols table (list of lists) filled with 0'seek
	
	tablecol = []
	table = []
	
	#Makes a row of 0's, ncols being the number of columns in the table
	
	
	#Stacks rows of 0's, nrows being the number of rows in the table
	for j in range(nrows):
		tablecol = []
		for i in range(ncols):
			tablecol.append(0)
		table.append(tablecol)
	
	#prints the table
	#printTable(table) #DB
	
	return table

def flipOptimization(dict, s1):
	##Input: Dictionary of flipped strings
	##Function:  Finds the best scored path of strings in the dictionary, and retains only those.
	##Output: Best scored path of strings in the dictionary, as a dictionary.
	
	dictKeys = sorted(dict.keys())
	dictValues = sorted(dict.values())
	scoreKeeper = []
	newdict = {}
	finishnewDict = False
	flipList = []
	#print(len(dictKeys)) #DB
	#print(dictValues) #DB
	positionSaver = []
	
	## For cleaning out errors where unscored strings are saved
	for i in range(len(dictKeys)):
		if len(dictValues[i]) < 3:
			positionSaver.append(i)
	
	for i in range(len(positionSaver)):
		positionDestroyer = positionSaver[len(positionSaver)-1-i] 
		#^Holds the position of empties as int, does so in reverse order to not disturb list
		
		dictKeys.pop(positionDestroyer)
		dictValues.pop(positionDestroyer)
	##
	
	for i in range(len(dictKeys)):
		scoreKeeper.append(dictValues[i][2]) #Looks for scores in dictionary
	maxVal = max(scoreKeeper)  #Takes the highest score of all the flip sequences
	
	for i in range(len(dictKeys)): 	#Places entry with highest score into new dictionary
		if dictValues[i][2] == maxVal:
			newKeyHolder = dictKeys[dictValues[i].index(maxVal)]
			#print(newKeyHolder)   #DB
			newdict[newKeyHolder] = dictValues[i]
	#print(maxVal)  #DB
	
	#Tracks backward from the highest score to make sure only one path is in the dictionary
	newdictKeys = sorted(newdict.keys())
	newdictValues = sorted(newdict.values())
	
	while finishnewDict == False:
			for i in range(len(newdictKeys)):
				#print(newdictValues[i][0])  #DB
				newdict[newdictValues[i][0]] = dict[newdictValues[i][0]]
				newdictKeys = sorted(newdict.keys())
				newdictValues = sorted(newdict.values())
				if newdictValues[i][0] == s1:
					finishnewDict = True
	
	sequenceList = newdictKeys
	for i in range(len(newdictKeys)):
		flipList.append(newdict[newdictKeys[i]][1])
	sequenceList.append(s1)
	
	#print(sequenceList) #DB
	#print(flipList) #DB
	#print(newdict) #DB
	return newdict, sequenceList, flipList
	
def singleFlipper(s1):  #Flips a single string.

	flippedString = ""
	
	for i in range(len(s1)+1):
		letter = s1[len(s1)-i:len(s1)-i+1]
		if letter == 'A':
			flippedString = flippedString + 'A'
		elif letter == 'T':
			flippedString = flippedString + 'T'
		elif letter == 'C':
			flippedString = flippedString + 'C'
		elif letter == 'G':
			flippedString = flippedString + 'G'
	
	#print("Flipped: ",flippedString)  #DB
	return flippedString
	
def bestPossibleScore(dict, s2): #Checks if the best possible score has been reached, and ends recursion early in that case.
	isBest = False
	dictKeys = sorted(dict.keys())
	
	for i in range(len(dictKeys)):
		if dictKeys[i] == s2:
			isBest = True
	return isBest

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
	graphspace_utils.postBio131Graph(edge_list,node_attrs,your_name+'-test')
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
	
## The lines below will call the main() function 
if __name__ == '__main__':
	main()