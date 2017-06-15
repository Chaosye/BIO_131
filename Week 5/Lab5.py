## Lab5
## Nick Egan

## Notes
# skew() mostly taken from HW4 work

import pylab

def main():
	##################################
	## INSTRUCTIONS:
	## First, make a small test string.
	## (A) Write a function to compute the skew, and call the function here.
	## (B) Copy the function to plot the skew, and call the function here.
	## (C) Then, read the E. coli genome and plot the skew.
	##################################
	
	genomeString = readFasta("e.coli.fasta")
	
	totaldiff = skew(genomeString)
	
	filename = "ecolifigure.png"
	
	plotLine(totaldiff, filename)
	
	return # done with the main() function.


## Define functions here
def skew(genomeString):
## Inputs: a string Genome
## Outputs: A list of integers calculating the running total of (#G-#C)

	#genomeString = "GCGCATGC"  #test
	totaldiff = []
	letterCounter = []
	stringCutter = ""
	counter = 0
	
	for i in range(len(genomeString)):
		stringCutter = genomeString[i:i+1]
		
		if stringCutter == "G":
			counter = counter + 1
			totaldiff.append(counter)
		elif stringCutter == "C":
			counter = counter - 1
			totaldiff.append(counter)
		#print("The found patterns were: ", totaldiff)    #DB
		#print("The list of letterCounter is: ", letterCounter)
		#print("For round ", i," the stringCutter is reading: ", stringCutter)
	
	print("totaldiff says: ", totaldiff)
	print("The counter is: ", counter)
	
	return totaldiff
	
	'''  A function for finding counters of individual letters in sequence.
	totaldiff = []
	letterList = []
	letterCounter = []
	removalCounter = 0
	
	for i in range(len(genomeString)):
		stringCutter = genomeString[i:i+1]
		letterList.append(stringCutter)
		letterCounter.append(0)
		
		for n in range(len(letterList)):
			if letterList[n] == stringCutter:
				letterCounter[n] = letterCounter[n] + 1
				break
		#print("The found patterns were: ", letterList)    #DB
		#print("The list of letterCounter is: ", letterCounter)
		#print("For round ", i," the stringCutter is reading: ", stringCutter)
		# cut apart string, then count repetitions of every sequence
	
	#----------------------------------
	#For cutting out repetitive patterns and their associated counters.
	positionSaver = [] #Holds the position of empty counters/repeating patterns
	
	for i in range(len(letterList)):
		if letterCounter[i] == 0:
			positionSaver.append(i)
	
	#print("positionSaver: ", positionSaver)  #DB

	
	for i in range(len(positionSaver)):
		positionDestroyer = positionSaver[len(positionSaver)-1-i] 
		#^Holds the position of empties as int, does so in reverse order to not disturb list
		
		letterCounter.pop(positionDestroyer)
		letterList.pop(positionDestroyer)
	print("Final Counter: ", letterCounter) #DB
	print("Final List: ", letterList) #DB
	
	# This will read out to a list in the order of ['A', 'G', 'C', 'T']
	
	totaldiff = letterCounter[1] - letterCounter[2]
	
	if totaldiff <= 0:
		totaldiff = 0 - totaldiff
		
	print("The total value of #G - #C is: ", totaldiff)
	
	return totaldiff
	'''

def plotLine(numList, filename):
## Input: a list of numbers, and a file name ending in .png
## Output: a png file with the line plotted, stored in the output file name.
	x = range(len(numList))
	y = numList
	
	pylab.plot(x,y)
	
	pylab.xlabel("X Label")
	pylab.ylabel("Y Label")
	pylab.title("Title")
	
	pylab.grid(True)  # Shows grid lines
	
	pylab.savefig(filename) # Saves figure as a .png file and opens it
	print("Wrote to", filename)
	pylab.close() # Closes figure
	
	return

def readFasta(infile):
## Input: a FASTA file name, containing a SINGLE record.
## Output: a string representing the sequence imported

	fileLines = open(infile,'r').readlines() # stores lines as a list
	sequence = ''
	for line in fileLines[1:len(fileLines)]:
		strippedLine = line.strip() # removes whitespace from line
		sequence = sequence + strippedLine
	return sequence

## The lines below will call the main() function 
if __name__ == '__main__':
	main()