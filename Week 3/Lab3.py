## Lab 3
## Hand in at the end of Lab
## Nick Egan, Tues Lab

def main():
	'''
	Main method.  This is where the bulk of the work gets done.
	(You can denote block comments as lines between triple quotes)
	'''

	## 1. Consider the following DNA sequence.  Create two variables that contain 
	## the complement of the DNA sequence and the reverse complement of the DNA
	## sequence.  Do this by hand.
	dna = 'CCCATGGTGGGGGGGGGGCAGTCCATAACCC'
	#dna = 'ATAGCATTGC'
	compdna = 'TATCGTAACG'
	revcompdna = 'GCAATGCTAT'
	print('DNA:',dna)
	print('Comp. DNA:',compdna)
	print('Rev. Comp. DNA:',revcompdna)

	## print the output of the two intermediate functions.
	print()
	print('Intermediate Functions:')
	print('complement():',complement(dna))
	print('reverse():',reverse(dna))

	## Compute the reverse complement
	print()
	computedSequence = reverseComplement(dna)
	
	print('reverseComplement():',computedSequence)
	
	## 5. Use an IF statement to print 'Correct Answer!' if the computed
	## sequence and the hand-written sequences match and 'Incorrect Answer'
	## otherwise.
	if computedSequence == revcompdna:
		print('Correct Answer!')
	else:
		print('Incorrect Answer...')
		
	return 

## 2. Write a function to return the complement of a string.
def complement(sequence):
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
	print('<#2 FILL IN HERE>')
	print('comp = ' + comp)
	return comp

## 3. Write a function to return the reverse of a string.
def reverse(sequence):
	rev = ''
	for i in range(len(sequence)):
		letter = sequence[len(sequence) - i-1:len(sequence) - i]
		rev = rev + letter
	print('<#3 FILL IN HERE>')
	print('rev = ' + rev)
	return rev

## 4. Write a function to compute the reverse complement
## of a string.  Return this string.
def reverseComplement(sequence):
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
	print('<#4 FILL IN HERE>')
	print('revcomp = ' + revcomp)
	return revcomp

## The lines below will call the main() function 
if __name__ == '__main__':
	main()