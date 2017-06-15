## HW3 Due Feb 17
## HW3 Out Feb 6
## HW3.1 internal deadline: Feb 10
## HW3.2 internal deadline: Feb 13

## ESTIMATED TIME:  13.1:   13.2:   13.3:
## NAME: Nick Egan
#Thank you so much, Anna!

## This line "reads" anna_functions.py and loads some functions that Anna has written.
import anna_functions

def main():
    '''
    This main() function converts the DNA sequence from a dataset into mRNA and 
    finally to a peptide sequence.
    Inputs: Nothing (set dataset variable below)
    Outputs: Nothing.
    '''

    testNeg = 'GGGTTATGGACTGCCCCCCCCCCACCATGGG'  #Rev. comp of DNA strand
	
    # Set dataset to one of the following strings: 'testPos','SRC','testNeg', or 'TMPRSS2'
    dataset = 'TMPRSS2'
    print('Dataset:',dataset)

    # Use the getData() function from anna_functions.py to get all the information
    # associated with a dataset.
    dna,exonStarts,intronStarts,strand,rnaFromFile,peptideFromFile = anna_functions.getData(dataset)

    # Print all the information associated with these variables.
    printInfo(dna,exonStarts,intronStarts,strand,rnaFromFile,peptideFromFile)
    
    # Transcribe the DNA to RNA.  
    if strand == '+':
        mRNA = transcribe(dna,exonStarts,intronStarts, strand)
    elif strand == '-':
        newExonStarts = []
        newIntronStarts = []
		#The below section reverses the exons/introns, using the arrayFlipper function.
        for i in range(len(exonStarts)):
            newExonStarts.append(len(dna) - exonStarts[i])
            #print(newExonStarts) #For debugging
        for i in range(len(intronStarts)):
            newIntronStarts.append(len(dna) - intronStarts[i])
            #print(newIntronStarts) #For debugging
        newExonStarts = arrayFlipper(newExonStarts)
        newIntronStarts = arrayFlipper(newIntronStarts)
		#----------------------------------------------------
        mRNA = transcribe(dna, newExonStarts, newIntronStarts,strand)
        #print(mRNA, "This is the negative mRNA") # For easier system output reading.
    if mRNA == rnaFromFile:
	    print("Your RNA is correct!")
    else:
	    print("Your RNA does not match!")

    ## Translate the mRNA to peptide
    computedPeptide = translate(mRNA)


    return # done with the main() function.

def arrayFlipper(array):
# For quickly reversing arrays
    newArray = []
    for i in range(len(array)):
        newArray.append(array[len(array)-1-i])
        #print(newArray) #For debugging
    return newArray
	
def printInfo(dna,exonStarts,intronStarts,strand,rna,peptide):
    '''
    Print information about the variables collected about a particular dataset.
    Inputs: 
        - dna: string representing the DNA sequence
        - exonStarts: list of integers representing the starts of the exons
        - intronStarts: list of integers representing the starts of the introns
        - strand: string for positive ('+') or negative ('-') orientation
        - rna: string representing the RNA sequence from the fasta file
        - peptide: string representing the peptide sequence from the fasta file
    Outputs: Nothing
    '''
	#notice error with TabError here - use spaces instead of tabs
    if len(dna) < 50:
        print("DNA: ", dna)
    else:
        print("DNA: ", len(dna), " nucleotides long.")
    print("Num exons: ", len(exonStarts))
    #print("Exon places*: ", exonStarts)
    #print("Num introns*: ", len(intronStarts))
    #print("Intron places*: ", intronStarts)
    print("strand: ", strand)
    print("RNA (from file): ", rna)
    print("peptide (from file): ", peptide)
	

    return # done with the printInfo() function

def transcribe(DNAsequence,exonStarts,intronStarts,strand):
    '''
    Converts a DNA sequence into an mRNA sequence.  
    Inputs: 
        - dna: string representing the DNA sequence
        - exonStarts: list of integers representing the starts of the exons
        - intronStarts: list of integers representing the starts of the introns
    Outputs: the mRNA string.
    '''
    
    premRNA = ''
	#Finding complement of DNA
    for i in range(len(DNAsequence)+1):
        letter = DNAsequence[i-1:i]
        if letter == 'A':
            premRNA = premRNA + 'A'
        elif letter == 'T':
            premRNA = premRNA + 'U'
        elif letter == 'C':
            premRNA = premRNA + 'C'
        elif letter == 'G':
            premRNA = premRNA + 'G'
	
    print("premRNA = ", premRNA)
	
	#Splicing out introns
    mRNA = ""
    for i in range(len(exonStarts)):
         if strand == '+':
            mRNA = mRNA + premRNA[exonStarts[i]:intronStarts[i]]
         elif strand == '-':
            mRNA = mRNA + premRNA[intronStarts[i]:exonStarts[i]]
         #print("mRNA in round ", i," is: ", mRNA)  #let's me know mRNA is adding onto string correctly
	
    print('Computed mRNA: ', mRNA)

    return mRNA # done with the transcribe() function.

def translate(mRNA):
    '''
    Converts an mRNA sequence into a peptide sequence.
    Inputs:
        - mRNA: string representing the mRNA sequence.
    Outputs:
        - peptide: string representing the amino acid sequence.
    '''
    #print (anna_functions.getAminoAcid('AAA'))
    #print (anna_functions.getAminoAcid('AUG'))
    #print (anna_functions.getAminoAcid('UAA')) Stop codon, reads as '*'
    #print (anna_functions.getAminoAcid('aug')) Lowercase is fine!
    #print (anna_functions.getAminoAcid('AU')) Wrong length
    #print (anna_functions.getAminoAcid('XYZ')) Not in dictionary
	
    testPeptide = "AUGAAATTTUAA"
    codonListing = list(range(0, len(mRNA), 3))
    #codonListing = list(range(0, len(testPeptide), 3))

    aaPrint = ''   # empty string that amino acid sequence will be printed to
	
    #print(codonListing)  #for making sure the codons are being read in sets of 3
    for i in range(len(codonListing)):
         aaPrint = aaPrint + anna_functions.getAminoAcid(mRNA[i*3:(i+1)*3])
		 #^converts codons into amino acids, adds to aaPrint string.
		 
         #print(testPeptide[i*3:(i+1)*3]) #makes sure correct RNA seq. is being imported
	
    print(aaPrint)
    peptide = ''

    return peptide # done with the translate() function.

## The lines below will call the main() function 
if __name__ == '__main__':
    main()
