## HW4
## Due 10am on Friday, February 24

##Nick Egan
#Time Estimate: 2 + 5 = 7 hours (unfinished)
##Unfinished portions:
## - cutting out non-existent patterns that are accounted for in the mismatch version
## - repeating patterns in the final frequentCounter for the mismatch version, how to remove?

#Notes:
#  #DB indicates lines used for debugging/info during runtime
#Citations:
#.count() found at stackoverflow.com/questions/2600191/
#max() and min() learned from Anna Ritz
#.pop() learned from stackoverflow.com/questions/627435/
#HammingDistanceFinder function is from solving Rosalind question 2.
#sequenceReverseComplementer function is from Lab 3.
# DB in comments stands for debug - for clarifying 

import itertools

def main():
	## The replication origin (oriC) of Vibrio Cholerae
	vc = 'ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC'
	
	## The replication origin (oriC) of Thermotoga petrophila
	rt ='AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGAAAAGAGGTGGTAAAAAA'
	
	## Make a test string.
	testString = 'GCGGCGCCGCGGCGCGCCGCGCGCGCGCGCGCCGCGCGCGGCGCGCG'
	
	chosenString = testString
	kmerLength = 5
	
	print('chosenString:', chosenString)
	
	frequentKmer = frequentWords(chosenString, kmerLength)
	print("The most frequently appearing k-mer is: ", frequentKmer)
	frequentKmer = frequentWordsWithReverseComplements(chosenString, kmerLength)
	print("Including reverse complements, the most frequently appearing k-mer is: ", frequentKmer)
	frequentKmer = frequentWordsWithMismatches(chosenString, 5, 1)
	print("Including mismatches, the most frequently appearing k-mer is: ", frequentKmer)
	## CALL your functions here (e.g., "wordList = frequentWords(inputs)")
	
	
	return # done with the main() function.


## WRITE your functions here (e.g. "def frequentWords(inputs)")
def frequentWords(Text, lenKmer):
	frequentKmer = []
	
	stringCutter = ""
	frequentList = []
	frequentCounter = []
	removalCounter = 0
	
	for i in range(len(Text)):
		stringCutter = Text[i:i+lenKmer]
		frequentList.append(stringCutter)
		frequentCounter.append(0)
		
		for n in range(len(frequentList)):
			if frequentList[n] == stringCutter:
				frequentCounter[n] = frequentCounter[n] + 1
				break
		#print("The found patterns were: ", frequentList)    #DB
		#print("The list of frequentCounter is: ", frequentCounter)
		#print("For round ", i," the stringCutter is reading: ", stringCutter)
		# cut apart string, then count repetitions of every sequence
	
	#----------------------------------
	#For cutting out repetitive patterns and their associated counters.
	positionSaver = [] #Holds the position of empty counters/repeating patterns
	
	for i in range(len(frequentList)):
		if frequentCounter[i] == 0:
			positionSaver.append(i)
	
	#print("positionSaver: ", positionSaver)  #DB

	
	for i in range(len(positionSaver)):
		positionDestroyer = positionSaver[len(positionSaver)-1-i] 
		#^Holds the position of empties as int, does so in reverse order to not disturb list
		
		frequentCounter.pop(positionDestroyer)
		frequentList.pop(positionDestroyer)
	#print("Final Counter: ", frequentCounter) #DB
	#print("Final List: ", frequentList) #DB
	
	#frequentKmer = frequentList[frequentCounter.index(max(frequentCounter))]
	#only grabs the first thing w/ max value, which is not good enough
	
	for i in range(len(frequentCounter)):
		if frequentCounter[i] == max(frequentCounter):
			#print(frequentList[i])
			frequentKmer.append(frequentList[i])
	

	return frequentKmer

def frequentWordsWithReverseComplements(Text, lenKmer):
	frequentKmer = []
	
	stringCutter = ""
	frequentList = []
	frequentCounter = []
	removalCounter = 0
	
	for i in range(len(Text)):
		stringCutter = Text[i:i+lenKmer]
		stringCutterRev = sequenceReverseComplementer(stringCutter)
		frequentList.append(stringCutter)
		frequentList.append(stringCutterRev)
		frequentCounter.append(0)
		frequentCounter.append(0)
		
		for n in range(len(frequentList)):
			if frequentList[n] == stringCutter:
				frequentCounter[n] = frequentCounter[n] + 1
				break
			if frequentList[n] == stringCutterRev:
				frequentCounter[n] = frequentCounter[n] + 1
				break
		#print("The found patterns were: ", frequentList)    #DB
		#print("The list of frequentCounter is: ", frequentCounter)
		#print("For round ", i," the stringCutter is reading: ", stringCutter)
		# cut apart string, then count repetitions of every sequence
	
	#----------------------------------
	#For cutting out repetitive patterns and their associated counters.
	positionSaver = [] #Holds the position of empty counters/repeating patterns
	
	for i in range(len(frequentList)):
		if frequentCounter[i] == 0:
			positionSaver.append(i)
	
	#print("positionSaver: ", positionSaver)  #DB

	
	for i in range(len(positionSaver)):
		positionDestroyer = positionSaver[len(positionSaver)-1-i] 
		#^Holds the position of empties as int, does so in reverse order to not disturb list
		
		frequentCounter.pop(positionDestroyer)
		frequentList.pop(positionDestroyer)
	#print("Final Counter: ", frequentCounter) #DB
	#print("Final List: ", frequentList) #DB
	
	#frequentKmer = frequentList[frequentCounter.index(max(frequentCounter))]
	#only grabs the first thing w/ max value, which is not good enough
	
	for i in range(len(frequentCounter)):
		if frequentCounter[i] == max(frequentCounter):
			#print(frequentList[i])
			frequentKmer.append(frequentList[i])
	

	return frequentKmer

def frequentWordsWithMismatches(Text, lenKmer, numMismatches):
	frequentKmer = []
	
	stringCutter = ""
	frequentList = []
	frequentCounter = []
	removalCounter = 0
	mismatchAddendum = 0
	patternChecker = []
	
	for i in range(len(Text)):
		stringCutter = Text[i:i+lenKmer]
		
		if len(stringCutter) < lenKmer: #Prevents short patterns
			break
		
		frequentList.append(stringCutter)
		frequentCounter.append(0)
		
		for n in range(len(frequentList)):
			if frequentList[n] == stringCutter:
				frequentCounter[n] = frequentCounter[n] + 1
				break
		#print("The found patterns were: ", frequentList)    #DB
		#print("The list of frequentCounter is: ", frequentCounter)
		#print("For round ", i," the stringCutter is reading: ", stringCutter)
		# cut apart string, then count repetitions of every sequence
	
	#Mismatch accounting section#
	for i in range(len(frequentList)):
		for n in range(len(frequentList)):
			mismatchAddendum = HammingDistanceFinder(frequentList[i], frequentList[n], len(frequentList[i]))
			if mismatchAddendum == 1: #requires that there be a difference for the counter addition
				frequentCounter[i] = frequentCounter[i] + 1
			#print(frequentList[i], " and ", frequentList[n])  #DB for short patterns
	#---------------------------#  Currently is recreating patterns?

	
	#For cutting out repetitive patterns and their associated counters.
	positionSaver = [] #Holds the position of empty counters/repeating patterns
	
	for i in range(len(frequentList)):
		if frequentCounter[i] == 0:
			positionSaver.append(i)
	
	#print("positionSaver: ", positionSaver)  #DB

	
	for i in range(len(positionSaver)):
		positionDestroyer = positionSaver[len(positionSaver)-1-i] 
		#^Holds the position of empties as int, does so in reverse order to not disturb list
		
		frequentCounter.pop(positionDestroyer)
		frequentList.pop(positionDestroyer)
	#print("Final Counter: ", frequentCounter) #DB
	#print("Final List: ", frequentList) #DB
	
	#frequentKmer = frequentList[frequentCounter.index(max(frequentCounter))]
	#only grabs the first thing w/ max value, which is not good enough
	
	for i in range(len(frequentCounter)):
		if frequentCounter[i] == max(frequentCounter):
			#print(frequentList[i])
			frequentKmer.append(frequentList[i])
			patternChecker.append(0)

	# Loop through all possible sets of k nucleotides to build the kmers...
	'''
	for prod in itertools.product("ACGT",repeat=5):
		kmer = "".join(prod) # kmer is a string
		print (kmer) # print the k-mer
	'''
	# counter that increases with each pattern checked against real string
	# add to counter if pattern does not equal pattern in DNA
	# if counter = total length of set, then remove pattern
	return frequentKmer
	
def sequenceReverseComplementer(sequence):
	revcomp = ''
	comp = ''
	for i in range(len(sequence)+1):
		letter = sequence[i-1:i]
		if letter == 'A':
			comp = comp + 'T'
		elif letter == 'T':
			comp = comp + 'A'
		elif letter == 'C':
			comp = comp + 'G'
		elif letter == 'G':
			comp = comp + 'C'
	
	for i in range(len(sequence)):
		letter = comp[len(sequence) - i-1:len(sequence) - i]
		revcomp = revcomp + letter
	
	return revcomp
	
def HammingDistanceFinder(seq1,seq2,len):
	HammingDistance = 0
	for i in range(len+1):
		letter1 = seq1[i-1:i]
		letter2 = seq2[i-1:i]
		
		if letter1 != letter2:
			HammingDistance = HammingDistance + 1
	return HammingDistance
	
## The lines below will call the main() function 
if __name__ == '__main__':
	main()