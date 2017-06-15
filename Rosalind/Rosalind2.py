#Rosalind BIO131 Course Set: Problem 2
#Nick Egan
import sys

def main():
	#Open and read from file.
	f = open("rosalind_ba1g.txt", "r")
	text = f.read()
	
	f.close()
	#print("Before Split")
	#print(text)
	text = text.split('\n')
	#print("After Split")
	#print(text)
	DNAList = text[0:2]
	sequence1 = DNAList[0]
	sequence2 = DNAList[1]
	
	print("Our first sequence is:  ", sequence1)
	print("Our second sequence is: ", sequence2)
	
	HammingDistance = 0
	
	if len(sequence1) == len(sequence2):
		length = len(sequence1)
	else:
		sys.exit("Sequences are different lengths!")
	
	HammingDistance = HammingDistanceFinder(sequence1,sequence2, length)
	#Debugger
	Debugger()
			
	print("The Hamming Distance of these two sequences is:", HammingDistance)

#Finds Hamming Distance by scanning through strings and comparing individual characters	
def HammingDistanceFinder(seq1,seq2,len):
	HammingDistance = 0
	for i in range(len+1):
		letter1 = seq1[i-1:i]
		letter2 = seq2[i-1:i]
		
		if letter1 != letter2:
			HammingDistance = HammingDistance + 1
	return HammingDistance
		
def Debugger():
	AAAATTTT = HammingDistanceFinder("AAAA", "TTTT", 4)
	
	if AAAATTTT != 4:
		sys.exit("Error with AAAA case")
		
		
## The lines below will call the main() function 
if __name__ == '__main__':
    main()