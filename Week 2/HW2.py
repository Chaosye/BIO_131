## HW2 (Due Feb 6)
## Nick Egan ( ´ ▽ ` )ﾉ

print('-------------------------------------------------------------')
print('1. Manipulating Numbers')
print('-------------------------------------------------------------')
print()

10+3*5           ## Line A
x = (1+4)*3      ## Line B
20+x             ## Line C
y = x            ## Line D
z = 2*x          ## Line E
x = x+1.0        ## Line F
x**y             ## Line G 
x = x + y + z    ## Line H
z = (x-1)/y      ## Line I

## 1.1: Replace '<STRING>' with the string 
## 'Assignment' or 'Expression'.

## 1.2. Replace '<VALS>' with the values of 
## x, y, and z. Be careful about which variables are 
## ints and which are floats.

print('After the Expression in line A, x/y/z do not exist.')
print('After the Assignment in line B, x = 15 and y/z do not exist.')
print('After the Expression in line C, x = 15 and y/z do not exist.')
print('After the Assignment in line D, x and y = 15, and z does not exist.')
print('After the Assignment in line E, x and y = 15, z = 30.')
print('After the Assignment in line F, x = 16.0, y = 15, z = 30.')
print('After the Expression in line G, x = 16.0, y = 15, z = 30.')
print('After the Assignment in line H, x = 61.0, y = 15, and z= 30.')
print('After the Assignment in line I, x = 61.0, y = 15, and z = 4.0.')
print()

print('-------------------------------------------------------------')
print('2. Lists')
print('-------------------------------------------------------------')

## 2.1.  Print the value in each variable name using ONLY indices
## into numList.
numList = [3,2,7,5]

## Here is an example.
shouldBe1 = numList[0]-numList[1]
print('An example: shouldBe1 =',shouldBe1)

## Replace the 0's with expressions that only use indices and operators.
shouldBe4 = numList[2] - numList[0]
print('shouldBe4 =',shouldBe4)

shouldBe10 = numList[0] + numList[2]
print('shouldBe10 =',shouldBe10)

shouldBe20 = numList[1]*(numList[0] + numList[2])
print('shouldBe20 =',shouldBe20)

shouldBe25 = numList[1]*(numList[0] + numList[2]) + numList[3]
print('shouldBe25 =',shouldBe25)

## 2.2. Put the classes you are currently taking into the
## mySchedule variable.
mySchedule = ['bio131', 'soc326', 'rel310', 'chem202', 'bio102']

## 2.2(a) Print the length of mySchedule
print('The length of mySchedule is: ' + str(len(mySchedule)))

## 2.2(b) Print the first and last items of mySchedule
print('The first and last items of mySchedule are: ' + mySchedule[0] + ' ' + mySchedule[-1])

## 2.2(c) Try the following line: print(mySchedule[len(mySchedule)]).
## What happens? Write your answer in the comments.

## My Answer: An "IndexError: list index out of range" error message is provided.  
## What this means is that a position of the list is called that doesn't have a value - in this case the 5th position of an index that goes from 0 to 4 is called, and so it can't be done.

## 2.3.  The range() function.
print()
print('Practice with the range() function.')

## 2.3(a) evaluate the following expressions.
#print(list(range(5)))
#print(list(range(10)))
#print(list(range(1)))

## 2.3(b) Use the range() function to print the indices of mySchedule.
print(list(range(len(mySchedule))))

print()
print('-------------------------------------------------------------')
print('3. FOR Loops')
print('-------------------------------------------------------------')
print()

## 3.1. Print the elements of numList:
print('The elements of numList are below.')
for i in range(len(numList)):
	print(numList[i])
print()

## 3.2. Print the elements of mySchedule:
print('The elements of mySchedule are below.')
for i in range(len(mySchedule)):
	print(mySchedule[i])
print()

## 3.3. Use a for loop to print the index of each element of mySchedule.
## Modify the code to print the value and the length as well.
print('The indices, as well as value and length, of mySchedule are below.')
for i in range(len(mySchedule)):
	print(str(i) + ' ' + mySchedule[i] + ', length:' + str(len(mySchedule)))


## 3.4. Use a for loop to count the number of elements.
numClasses = 0
for i in range(len(mySchedule)):
	numClasses = numClasses + 1
print('numClasses = ' + str(numClasses))

print('-------------------------------------------------------------')
print('4. Write a Change Counter')
print('-------------------------------------------------------------')

## coinDenominations contains four values: one each for a
## penny, a nickel, a dime, and a quarter.
coinDenominations = [1,5,10,25]
print('coinDenominations:',coinDenominations)

## numberOfCoins contains four values: the number of pennies, nickels,
## dimes, and quarters you find in your pocket.  You may have 0 coins of some
## denomination.
numberOfCoins = [3,1,0,2]
print('numberOfCoins',numberOfCoins)

## dollarAmount is the number of dollars you have.
dollarAmount = 0
for i in range(4):
	dollarAmount = dollarAmount + (numberOfCoins[i] * (coinDenominations[i]/100))

## print the dollar amount.
print('The dollar amount is: $',dollarAmount)

print('-------------------------------------------------------------')
print('5. String Slices')
print('-------------------------------------------------------------')

## Evaluate the lines from the instructions.
stringOfNumbers = '0123456789'
print(stringOfNumbers)
print(stringOfNumbers[5]) # 6th element 5
print(stringOfNumbers[3:5]) #3rd and 4th element 34
print(stringOfNumbers[3:6]) #3rd to 5th element 345
print(stringOfNumbers[:5]) #elements 5th and under 01234
print(stringOfNumbers[5:]) #elements 6th and over 56789
print(stringOfNumbers[:5] + '*' + stringOfNumbers[5:]) #01234*56789

print('-------------------------------------------------------------')
print('6. Hypothetical Gene')
print('-------------------------------------------------------------')

hypotheticalgene = 'eeeeeeeeeeeiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiieeeeeee'
print('\nhypothetical gene:',hypotheticalgene)

## These variables represent the index of the start of each exon, the 
## intron, and the length of the gene.
exon1start = 0
intron1start = 11
exon2start = 43
genelen = len(hypotheticalgene)

## 6.1. Print the lengths of the exons using the start and genelen variables
print('The length of the exons are: ', (intron1start + genelen - exon2start)) 

## 6.2. Store strings corresponding to the exons and the intron.
## Assign variables to strings that correspond to exon1, exon2, and the intron.
exon1 = hypotheticalgene[:intron1start] #Checked with intron1start+1
exon2 = hypotheticalgene[exon2start:] #Checked with exon2start-1
intron = hypotheticalgene[intron1start:exon2start] #Checked with intron1start-1:exon2start+1

## 6.3.  Print the length of hypotheticalgene and the sum of the exons + intron.
print()
print('The length of the gene is: ', genelen)
print('The sum length of the exons and intron is: ', len(exon1)+len(intron)+len(exon2))


print('-------------------------------------------------------------')
print('7. Extra Exercises (Optional)')
print('-------------------------------------------------------------')

## Exon Starts and Intron Starts as lists
exonstarts = [exon1start,exon2start]
intronstarts = [intron1start, genelen]
for i in range(2):
	print('Exon #', (i+1) , ' ' + hypotheticalgene[exonstarts[i]:intronstarts[i]])

## Exon/Intron Starts for the SRC Gene
SRCexonstarts = [0,1546,3471,11291,11570,13558,15095,17511,18998,19831,20145,20567]
SRCintronstarts = [183,1800,3571,11390,11674,13708,15251,17691,19075,19985,20277,22829]

#Print the number of exons for SRC
print('Number of exons for SRC: ', len(SRCexonstarts))

#Print the average exon length
averageExSRC = []
for i in range(len(SRCexonstarts)):
	averageExSRC = averageExSRC + [SRCintronstarts[i] - SRCexonstarts[i]]
finalAvgeExSRC = (sum(averageExSRC)/len(averageExSRC))
print('Average exon lengths: ' + '%.2f' % finalAvgeExSRC)  #( '%.2f' % variable) - allows the rounding of the variable to 2 spaces
#^ checked in pythontutor

#Print the average intron length
averageInSRC = []
for i in range(len(SRCintronstarts)-1):
	averageInSRC = averageInSRC + [SRCexonstarts[i+1] - SRCintronstarts[i]]
finalAvgeInSRC = (sum(averageInSRC)/len(averageInSRC))
print('Average intron lengths: ' + '%.2f' % finalAvgeInSRC)
#^checked in pythontutor

#Print the variance in exon lengths
variance = 0     #Calculates value of variance from (sum of sumList/)length-1
sumList = []    #collects (items-mean)^2

for i in range(len(SRCexonstarts)):
	sumList = sumList + [(((SRCintronstarts[i]-SRCexonstarts[i]) - finalAvgeExSRC)**2)]
	#print(sumList)
variance = sum(sumList)/(len(SRCexonstarts)-1)
print('The variance in exon lengths is: ' + '%.2f' % variance)

#Print the variance in intron lengths
variance = 0
sumList = []

for i in range(len(SRCintronstarts) - 1):
	sumList = sumList + [(((SRCexonstarts[i+1] - SRCintronstarts[i]) - finalAvgeInSRC)**2)]
	#print(sumList)
variance = sum(sumList)/(len(SRCintronstarts)-2)
print('The variance in intron lengths is: ' + '%.2f' % variance)
	
## When you're done, uncomment the line below.
print()
print('Done with HW2!')
print()
print('When you\'re done, write the approximate amount of time spent in the comments.')
## Approximate Time Spent: 50 min (+ 50 min for Extra Exercises)
