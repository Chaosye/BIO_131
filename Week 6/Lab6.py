## Lab6
## Nick Egan

import pylab

def main():

    ## Run the warmup().
    warmup()
    
    motifList = getBindingSites("toy-motifs.txt")

    countListings = computeCounts(motifList)

    computeFrequencies(countListings)

    print('Done!')
    return # done with main() function

def warmup():
    strMat = ['abc','def','ghi','jkl']
    print('strMat:',strMat)
    print("\nBeginning of warmup!\n")
    #for printing out by individual line
    print("Individual lines of strMat:")
    for i in range(len(strMat)):
        print(strMat[i])
	
	#for printing out every letter on individual lines
    print("Lines separated by character for strMat:")
    for i in range(len(strMat)):
        for n in range(len(strMat[i])):
            Text = strMat[i]
            print(Text[n:n+1])
	
    Text = ""
    #for printing out letters, grouped by their position in a string, assuming equal length of string throughout.
    print("Lines separated by letter position in string:")
    for i in range(len(strMat[0])):
        for n in range(len(strMat)):
            textCutter = strMat[n]
            Text = Text + textCutter[i:i+1]
        print(Text)
        Text = ""
	
    print('\nDone with warmup.\n')
    return

## Write any other functions you need here.  

## Given a file name, reads the list of binding sites and
## returns a list of strings.moif
def getBindingSites(fileName):
    myFile = open(fileName,'r') ## open the file
    lineString = myFile.read() ## Read the file into one long string
    myFile.close() ## close the file
    lineString = lineString.strip() ## remove extra whitespace
    lineList = lineString.split('\n') ## Split the string
    print('\nMotifs:')
    for pattern in lineList:
        print(pattern)
    return lineList

def computeCounts(motifList):
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
    print("A: ", aCounter)
    print("C: ", cCounter)
    print("G: ", gCounter)
    print("T: ", tCounter)
    finalCounter.append(aCounter)
    finalCounter.append(cCounter)
    finalCounter.append(gCounter)
    finalCounter.append(tCounter)
	
    print("finalCounter: ", finalCounter)
	
    return finalCounter
	
def computeFrequencies(countListings):
    positionSum = []
    tempfreqHolder = []
    freqHolder = []
    tempSum = 0.0
    for i in range(len(countListings[0])):
        for n in range(len(countListings)):
            tempSum = tempSum + countListings[n][i]
            tempfreqHolder.append(countListings[n][i]/len(countListings[0]))
        freqHolder.append(tempfreqHolder)
        tempfreqHolder = []
        positionSum.append(tempSum)
        tempSum = 0.0
    print(positionSum)
    print(freqHolder)
    return

def computeConsensus(freqListings):
    
    return

#################################################
## This function takes a list of numbers and a string
## that ends in '.png', makes and saves a bar chart.
## Inputs: list of numbers (floats and/or ints), a string that ends in ".png"
## Returns: nothing
def plotMotif(frequencyMat,pngname):
    ## runnnigF is the "starting points" of the next color's plot
    ## to make a "stacked bar chart"
    runningF = [0]*len(frequencyMat[0])
    colors = {'A':'g','C':'b','G':'y','T':'r'}
    letterList = ['A','C','G','T']
    inds = range(len(runningF))
    ## For each row in table (A/C/G/T)
    for i in range(len(frequencyMat)):
        ## Make bar plots with a particular color.
        pylab.bar(inds,frequencyMat[i],0.9,color=colors[letterList[i]],bottom=runningF)
        ## Add these values to runningF
        for j in range(len(runningF)):
            runningF[j] += frequencyMat[i][j]
   
    ## Otherwise, set labels/title according to 
    ## Frequency.
    pylab.ylabel('Frequency')
    pylab.title('Frequency Logo of Motif')
    pylab.ylim(0,1)

    ## Write the legend
    pylab.legend(letterList)
    ## The x-limits always range from 0 to the # of positions.
    pylab.xlabel('Motif Position')
    pylab.xlim(0,len(frequencyMat[0]))
    pylab.xticks([i+0.5 for i in range(len(frequencyMat[0]))],range(1,len(frequencyMat[0])+1))
    
    ## Save the figure.
    pylab.savefig(pngname)
    print('Wrote to',pngname)
    pylab.close()
    return
#################################################

if __name__ == '__main__':
    main()