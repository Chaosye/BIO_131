#.count() found at stackoverflow.com/questions/2600191/
#max() and min() learned from Anna Ritz
#.pop() learned from stackoverflow.com/questions/627435/
# DB in comments stands for debug - for clarifying print statements mostly.

def main():
	testText = "GCGCGCGCGCGGGCGCCCGCGGCGGCGCCGCGCGCGCGGGCCGGCCGCGCGCGGGCCG"
	testPattern = 'GCG'
	testk = 3
	
	patternCounter = PatternCount(testText, testPattern)
	print("The number of times the pattern appears in the text is: ", patternCounter)
	
	frequentKmer = OneFrequentWord(testText, testk)
	print("The most frequently appearing k-mer is: ", frequentKmer)
	
	return

def PatternCount(Text, Pattern):
	
	patternCounter = 0
	
	stringCutter = ""
	
	for i in range(len(Text)):
		stringCutter = Text[i:i+len(Pattern)]
		if stringCutter == Pattern:
			patternCounter = patternCounter + 1
		#print("For round ", i," the stringCutter is reading: ", stringCutter) #DB
	return patternCounter

#what do you want out of this?
#given a string to read off, and a length, you want to find the most frequent pattern
#to do this, make two arrays, one that contains the pattern, and one that counts
##they should have the same indices
#if a pattern that has previously occurred is detected, it is not added, but is counted up

	
def OneFrequentWord(Text, lenKmer):
	
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
	print("Final Counter: ", frequentCounter) #DB
	print("Final List: ", frequentList) #DB
	
	#frequentKmer = frequentList[frequentCounter.index(max(frequentCounter))]
	#only grabs the first thing w/ max value, which is not good enough
	
	for i in range(len(frequentCounter)):
		if frequentCounter[i] == max(frequentCounter):
			#print(frequentList[i])
			frequentKmer.append(frequentList[i])
	
	return frequentKmer
	
def FrequentWords():
	
	return

if __name__ == '__main__':
	main()