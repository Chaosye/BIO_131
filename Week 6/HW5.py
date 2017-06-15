## HW5 - Implementing a Greedy Motif Finder
## Due 10am on Wed., 3/8/17

# Unfinished Portions:
# - Didn't get to the point generator, or most of the Greedy Algorithm, took an unreasonably long time fixing bugs on the frequency table.


## Nick Egan
# Time Estimate: 4

#Notes:
#  #DB indicates lines used for debugging/info during runtime
#Citations:
# computeCounts, and computeFrequencies come from work during Lab6.
# Some of GreedyMotifSearch comes from HW4

import pylab

def main():
	
	#motifString = getBindingSites("simulated-motifs.txt")
	motifString = ["ACCCCGTCCCCC","ACCGTCCCCCCC","ACCCCGTCCCCT"]   #DB test strings
	bestMotif = []
	
	for i in range(len(motifString)):
		bestMotif.append(GreedyMotifSearch(motifString[i], 5, i))  #Creates an array of bestMotifs, while also keeping track of line number with i
		
	print("HW5 has finished running.  Have a nice day!")
	return # ends main function

def getBindingSites(fileName):
#Input: filename, and file
#Output: text of file
    myFile = open(fileName,'r') ## open the file
    lineString = myFile.read() ## Read the file into one long string
    myFile.close() ## close the file
    lineString = lineString.strip() ## remove extra whitespace
    lineList = lineString.split('\n') ## Split the string
    print('\nMotifs:')
    for pattern in lineList:
        print(pattern)
    return lineList

def GreedyMotifSearch(strand, k, lineCounter):
	#Input: a single strand of DNA, length of motif
	#Output: a string - the single motif with highest score
	
	stringCutter = ""
	bestMotifs = ""
	motifList = []
	frequencyList = []
	countsArray = []
	
	for i in range(len(strand)):
	#Loop used to cut a bunch of k-mers
		stringCutter = strand[i:i+k]
		
		if len(stringCutter) < k: #Prevents short patterns
			break
		
		if i == 0:
			bestMotifs = stringCutter #First k-mer is the first bestMotifs
		
		motifList.append(stringCutter)
		#print("The found motifs were: ", motifList)    #DB
		#print("For round ", i," the stringCutter is reading: ", stringCutter) #DB
		# cut apart string, then count repetitions of every sequence
	countsArray = computeCounts(motifList)  
	frequencyList.append(computeFrequencies(countsArray, lineCounter))
	#motifPointGenerator(motifList, frequencyList)
	
	return bestMotifs

def computeCounts(motifList):
#Input: a list of strings
#Output: counts of all the appearances of [A,C,G,T] in those strings, per index position.
    aCounter = []
    cCounter = []
    gCounter = []
    tCounter = []
    finalCounter = []
    for i in range(len(motifList[0])):
        aCounter.append(0)
        cCounter.append(0)
        gCounter.append(0)
        tCounter.append(0)

    for i in range(len(motifList)):
        stringCutter = motifList[i]

        for n in range(len(stringCutter)):
            characterSelector = stringCutter[n:n+1]
            if characterSelector == "A":
                aCounter[n] = aCounter[n] + 1
            elif characterSelector == "C":
                cCounter[n] = cCounter[n] + 1
            elif characterSelector == "G":
                gCounter[n] = gCounter[n] + 1
            elif characterSelector == "T":
                tCounter[n] = tCounter[n] + 1
    print("\nA: ", aCounter)     #DB
    print("C: ", cCounter)     #DB
    print("G: ", gCounter)     #DB
    print("T: ", tCounter)     #DB
    finalCounter.append(aCounter)
    finalCounter.append(cCounter)
    finalCounter.append(gCounter)
    finalCounter.append(tCounter)
	
    #print("finalCounter: ", finalCounter)     #DB
	
    return finalCounter
	
def computeFrequencies(countListings, motifNumber):
#Input: counter array for the # of appearances of a letter in a string, and which line in order the motif is
#Process: sums up all the counters, and divides by position
#Output: determines the frequency of appearance of individual letters out of all letters in the counter array
    positionSum = []
    tempfreqHolder = []
    freqHolder = []
    tempSum = 0.0
    for i in range(len(countListings[0])):
        for n in range(len(countListings)):
		# Loop calculates sum of nucleotide appearances in a position
            tempSum = tempSum + countListings[n][i]
            tempfreqHolder.append(countListings[n][i])
        #print(tempSum)  #DB
        for n in range(len(countListings)):
		# Loop turns counters into probabilities across nucleotides in one position
            tempfreqHolder[n] = tempfreqHolder[n]/tempSum
        freqHolder.append(tempfreqHolder)
        tempfreqHolder = []
        positionSum.append(tempSum)
        tempSum = 0.0
    #print(positionSum)   #DB for making sure all characters are counted for each position
    print("\nThe number of occurrences of nucleotide per position in motif line number ", motifNumber," are: ", freqHolder)
    return freqHolder


def motifPointGenerator(motif, freq):
	#Input: a string motif, and a frequency array per index position in the string
	#Process: will produce a probability of that string occurring
	#Output: a float that is this probability that assigns a value to that motif
	
	profileHolder = []
	
	'''
	for i in range(len(freq)):
		
	'''
	return points

## The lines below will call the main() function 
if __name__ == '__main__':
	main()