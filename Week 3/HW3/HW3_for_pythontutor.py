## HW3 for pythontutor
## Contains overall structure of program.

def main():
    # some simple data for testing with pythontutor.org.
    dna = 'ATGTAA'
    exonStarts = [0,3]
    intronStarts = [3,5]
    strand = '+'
    rnaFromFile = 'AUGUAA'
    peptideFromFile = 'M*'

    # Print all the information associated with these variables.
    printInfo(dna,exonStarts,intronStarts,strand,rnaFromFile,peptideFromFile)
    
    # Transcribe the DNA to RNA.  
    mRNA = transcribe(dna,exonStarts,intronStarts)
    
    ## Translate the mRNA to peptide
    computedPeptide = translate(mRNA)

    return # done with the main() function.

def printInfo(dna,exonStarts,intronStarts,strand,rna,peptide):
    print('In PrintInfo() function')
    print('<FILL IN>')
    print('Done with PrintInfo() function')
    print()
    return # done with the printInfo() function

def transcribe(DNAsequence,exonStarts,intronStarts):
    print('In transcribe() function')
    print('<FILL IN>')
    print('Done with transcribe() function')
    print()
    return '' # done with the transcribe() function.

def translate(mRNA):
    print('In translate() function')
    print('<FILL IN>')
    print('Done with translate() function')
    print()
    return '' # done with the translate() function.

## The lines below will call the main() function
## Always put these lines at the BOTTOM of your file.
if __name__ == '__main__':
    main()
