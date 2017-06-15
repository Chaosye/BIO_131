## HW6
## Due Wed 4/12 at 10:00 AM

##Notes:
#DB indicates lines used for debugging/info during runtime
#Adding a comma to the left lets you pull in multiple variables from a method

##Citations:
#LCS(), printTable(), and initialize_table() are from Lab 8.
#map() function from https://stackoverflow.com/questions/15917076/how-to-return-the-highest-value-from-a-multi-dimensional-array
#end= as a modifier for print() from https://stackoverflow.com/questions/12032214/print-new-output-on-same-line

##Questions:
#How do I find the missing letters when taking a taxi? (e.g. PLEASANT becomes ASANT when cut down by LocalAlignment - taxi is not acknowledged and to what distance
#How do you set it up so that it can take a taxi in the middle of the alignment?

################################
## Nick Egan
## Estimate time spent: 4 + 2 + 1 = 7
################################

#import anna_functions  #thought i was making my own codons lol

def main():
	
	inittable = initialize_table(5, 5)
	blosum62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

	
	string1 = "ATGTTATA"   #Vertical
	string2 = "ATCGTCC"  #Horizontal
	peptide1 = "PLEASANTLY"  #Vertical
	peptide2 = "MEANLY"  #Horizontal
	
	
	#print("Vertical string is: ", string1)   #DB
	#print("Horizontal string is: ", string2) #DB

	LCSAlign, LCSScore = LCS(string1,string2)
	LCS_Alignment1, LCS_Alignment2 = backtrackAlignment(LCSAlign, string1, string2)
	
	GlobalAlign, GlobalScore = GlobalAlignment(string1, string2, 0, 1, 1)
	Global_Alignment1, Global_Alignment2 = backtrackAlignment(GlobalAlign, string1, string2)
	
	LocalAlign, LocalScore = LocalAlignment(string1, string2, 1, 1, 1, 10)
	Local_Alignment1, Local_Alignment2 = backtrackAlignment(LocalAlign, string1, string2)
	
	LocalAlignScores, LocalScoreWithScores = LocalAlignmentWithScores(peptide1, peptide2, 5, blosum62)
	LocalScores_Alignment1, LocalScores_Alignment2 = backtrackAlignment(LocalAlignScores, peptide1, peptide2)

	print("\nAll the alignments and scores created were:")
	print("\nLCS Alignment: \n", LCS_Alignment1,"\n", LCS_Alignment2)
	print("Score: ", LCSScore)
	print("\nGlobal Alignment: \n", Global_Alignment1,"\n", Global_Alignment2)
	print("Score: ", GlobalScore)
	print("\nLocal Alignment: \n", Local_Alignment1,"\n", Local_Alignment2)
	print("Score: ", LocalScore)
	print("\nLocal Alignment for PLEASANTLY and MEANLY: \n", LocalScores_Alignment1,"\n", LocalScores_Alignment2)
	print("Score: ", LocalScoreWithScores)
	
	#Changing the peptide and doing a new local alignment
	peptide1 = "PLEASANT"
	peptide2 = "MEANLY"
	
	LocalAlignScores, LocalScoreWithScores = LocalAlignmentWithScores(peptide1, peptide2, 5, blosum62)
	LocalScores_Alignment1, LocalScores_Alignment2 = backtrackAlignment(LocalAlignScores, peptide1, peptide2)
	
	print("\nLocal Alignment for PLEASANT and MEANLY: \n", LocalScores_Alignment1,"\n", LocalScores_Alignment2)
	print("Score: ", LocalScoreWithScores)

	
	return
	
def LCS(string1, string2):
	#INPUT: Two strings, s1 and s2
	#OUTPUT: The length of the longest common subsequence between s1 and s2
	
	#print("\nStart of LCS")
	
	LCSTable = []
	bestOption = 0
	holder = []
	
	#Creates a blank table in the lengths of strings + 1
	LCSTable = initialize_table(len(string2)+1,len(string1)+1)
	LCSBacktrack = initialize_table(len(string2)+1,len(string1)+1)
	#printTable(LCSTable)
	
	#score of +1 for a diagonal movement, score of 0 for a hor/vert movement
	for i in range(len(string1)+1):
		for j in range(len(string2)+1):
			holder = []
			directionality = []
			if i > 0:
				holder.append(LCSTable[i-1][j])
				directionality.append("s")
			if j > 0:
				holder.append(LCSTable[i][j-1])
				directionality.append("e")

			if i > 0 and j > 0:
				if string1[i-1] == string2[j-1]:
					holder.append(LCSTable[i-1][j-1]+1)
					directionality.append("d")
				else:
					holder.append(LCSTable[i][j])
					directionality.append("d")
				
			#print(i,j,holder,directionality)    #DB   see possible directions out of a node and their respective # of points
			if i != 0 and j != 0:
				LCSTable[i][j] = max(holder)
			if i == 0 and j == 0:
				LCSBacktrack[i][j] = "*"
			elif max(holder) == holder[0]:
				LCSBacktrack[i][j] = directionality[0]
			elif max(holder) == holder[1]:
				LCSBacktrack[i][j] = directionality[1]
			elif max(holder) == holder[2]:
				LCSBacktrack[i][j] = directionality[2]
			
	longest = max(map(max, LCSTable))  #DB   Finds the largest value of all spots in the table.
	#print(longest)  #DB  Seeing what the highest score in the table is/LCS
	
	#printTable(LCSTable, string1, string2)   #DB
	
	#LCSBacktrack[i][j] = 99  #DB  Making sure that the tables don't point to the same pointer
	#printTable(LCSBacktrack, string1, string2)  #DB
	
	return LCSBacktrack, longest
	
def GlobalAlignment(string1, string2, indel, matchscore, mismatchpenalty):
	#INPUT: strings s1 and s2, and three integers indel, matchscore, and mismatchpenalty
	#OUPUT: score of the optimal global alignment and the alignment itself,
	
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
	
	return GlobalBacktrack, longest

def LocalAlignment(string1, string2, indel, matchscore, mismatchpenalty, locallength):
	#INPUT: strings s1 and s2, and three integers indel, matchscore, and mismatchpenalty
	#OUPUT: score of the optimal Local alignment and the alignment itself,
	
	taxiride = False
	#print("\nStart of LocalAlignment.\n")   #DB
	
	LocalTable = []
	bestOption = 0
	LocalHolder = []
	
	#Creates a blank table in the lengths of strings + 1
	LocalTable = initialize_table(len(string2)+1,len(string1)+1)
	LocalBacktrack = initialize_table(len(string2)+1,len(string1)+1)

	
	for i in range(len(string1)+1):
		for j in range(len(string2)+1):
			LocalHolder = []
			directionality = []
			
			if i > 0:
				LocalHolder.append(LocalTable[i-1][j] - indel)
				directionality.append("s")
			if j > 0:
				LocalHolder.append(LocalTable[i][j-1] - indel)
				directionality.append("e")

			if i > 0 and j > 0:
				if string1[i-1] == string2[j-1]:
					LocalHolder.append(LocalTable[i-1][j-1] + matchscore)
					directionality.append("d")
				else:
					LocalHolder.append(LocalTable[i][j] - mismatchpenalty)
					directionality.append("d")
				
			#print(i,j,LocalHolder,directionality)     #DB    see possible directions out of a node and their respective # of points
			if i != 0 and j != 0:
				LocalTable[i][j] = max(LocalHolder)
			if i == 0 or j == 0:
				LocalBacktrack[i][j] = "*"
			elif max(LocalHolder) == LocalHolder[0]:
				LocalBacktrack[i][j] = directionality[0]
			elif max(LocalHolder) == LocalHolder[1]:
				LocalBacktrack[i][j] = directionality[1]
			elif max(LocalHolder) == LocalHolder[2]:
				LocalBacktrack[i][j] = directionality[2]
			elif max(LocalHolder) == 0:
				LocalBacktrack[i][j] = "*"
		
	longest = max(map(max, LocalTable))
	#print(longest)    #DB
	
	#printTable(LocalTable, string1, string2)
	#printTable(LocalBacktrack, string1, string2)
	
	return LocalBacktrack, longest

def LocalAlignmentWithScores(string1, string2, indel, biosum62):
	#INPUT: strings s1 and s2, and three integers indel, matchscore, and mismatchpenalty
	#OUPUT: score of the optimal Local alignment and the alignment itself,
	
	taxiride = False
	#print("\nStart of LocalAlignment.\n")   #DB
	
	LocalTable = []
	bestOption = 0
	LocalHolder = []
	
	#Creates a blank table in the lengths of strings + 1
	LocalTable = initialize_table(len(string2)+1,len(string1)+1)
	LocalBacktrack = initialize_table(len(string2)+1,len(string1)+1)

	
	for i in range(len(string1)+1):
		for j in range(len(string2)+1):
			LocalHolder = []
			directionality = []
			
			if i > 0:
				LocalHolder.append(LocalTable[i-1][j] - indel)
				directionality.append("s")
			if j > 0:
				LocalHolder.append(LocalTable[i][j-1] - indel)
				directionality.append("e")

			if i > 0 and j > 0:
				if string1[i-1] == string2[j-1]:
					LocalHolder.append(LocalTable[i-1][j-1] + biosum62[string1[i-1]][string2[j-1]])
					directionality.append("d")
				else:
					LocalHolder.append(LocalTable[i][j] - biosum62[string1[i-1]][string2[j-1]])
					directionality.append("d")
				
			#print(i,j,LocalHolder,directionality)     #DB    see possible directions out of a node and their respective # of points
			if i != 0 and j != 0:
				LocalTable[i][j] = max(LocalHolder)
			if i == 0 or j == 0:
				LocalBacktrack[i][j] = "*"
			elif max(LocalHolder) == LocalHolder[0]:
				LocalBacktrack[i][j] = directionality[0]
			elif max(LocalHolder) == LocalHolder[1]:
				LocalBacktrack[i][j] = directionality[1]
			elif max(LocalHolder) == LocalHolder[2]:
				LocalBacktrack[i][j] = directionality[2]
			elif max(LocalHolder) == 0:
				LocalBacktrack[i][j] = "*"
		
	longest = max(map(max, LocalTable))
	#print(longest)     #DB
	
	#printTable(LocalTable, string1, string2)
	#printTable(LocalBacktrack, string1, string2)
	
	return LocalBacktrack, longest
	
def backtrackAlignment(backtrack, string1, string2):
	#INPUT: backtrack table, and the two aligned strings.
	seqCounter = 0
	align1 = ""
	align2 = ""
	
	i = len(string1)  #Vertical rows
	j = len(string2)  #Horizontal col
	
	revpath = []   #Path read backwards from the end of the backtrack table
	path = []   #Path from start to finish of alignment.
	
	startingposition = backtrack[i][j]  #Takes the letter designated at the final step of the path
	newposition = ""  #Above, but updates with every step of the path - used to end pathbuilding.
	
	#print(string1)   #DB For making sure it's reading correctly
	#print(string2)   #DB
	
	
	while newposition != "*" :  #As long as the read position is not the first or a taxicab!
		#print("Backtrack is currently: ", backtrack[i][j])  #DB
		#print("seqCounter = ",seqCounter)    #DB
		if backtrack[i][j] == "d":
			align1 = string1[i-1] + align1
			align2 = string2[j-1] + align2
			i = i - 1 ; j = j - 1


		elif backtrack[i][j] == "s":
			align1 = string1[i-1] + align1
			align2 = "-" + align2
			i = i - 1
			
		elif backtrack[i][j] == "e":
			align1 = "-" + align1
			align2 = string2[j-1] + align2
			j = j - 1
		
		newposition = backtrack[i][j]  #Moves the position that's currently being read

		
	#print("Final align1: ", align1)   #DB
	#print("Final align2: ", align2)   #DB
	
	return align1, align2
	
def printTable(table, vertstring, horizstring):
	print(" ", end =  "     ")
	
	#Prints out the horizontal line across the top, used for DB
	for col in range(len(horizstring)):
		print(horizstring[col:col+1], end = "  ")  #DB
	print(" ")  #ends the 'end=' dominance for printing on the same line
	
	#Prints out the table, as the vertical string line by line.
	for row in range(len(table)):
		if row == 0:
			print(" ", table[row])
		else:
			print(vertstring[row-1:row], table[row])
	print('')
	return
	
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
	

## The lines below will call the ma
	
## The lines below will call the main() function 
if __name__ == '__main__':
	main()