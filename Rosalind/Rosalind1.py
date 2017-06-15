#Rosalind BIO131 Course Set: Problem 1
#Nick Egan

def main():
	# Initiate variables!
	testDNA = "ATCGATCG"
	countA = 0
	countC = 0
	countG = 0
	countT = 0
	
	sequence = "" # Insert sequence here
	#Loop for reading a string, and then adding to nucleotide counters.
	for i in range(len(sequence)+1): # Verified with testDNA :]
		letter = sequence[i-1:i]
		if letter == 'A':
			countA = countA + 1
		elif letter == 'C':
			countC = countC + 1
		elif letter == 'G':
			countG = countG + 1
		elif letter == 'T':
			countT = countT + 1
	print(countA, " ", countC, " ", countG, " ", countT, " ")

## The lines below will call the main() function 
if __name__ == '__main__':
    main()