## Functions for HW3
## Written by Anna Ritz
## Last Edited Feb 5, 2016
import sys

#######################################################
## Functions to Manipulate Datasets
#######################################################

def getData(dataset):
    '''
    Given a dataset name, returns five things:
      - DNA string 
      - exonStarts list
      - intronStarts list
      - strand string (either '+' or '-')
      - mRNA string (for comparison)
      - peptide string (for comparison)

    NOTE: The datafiles/ directory must be in the same location as the .py file.
    '''
    sequenceFile = 'datafiles/'+dataset+'-sequences.fasta'
    dna,rna,peptide = readFasta(sequenceFile)
    ## add a STOP codon to the peptide sequence.
    peptide = peptide + '*'

    tablefile = 'datafiles/'+dataset+'-exon-info.txt'
    exonStarts,intronStarts,strand = readTable(tablefile)
    
    return dna,exonStarts,intronStarts,strand,rna,peptide


def readTable(infile):
    '''
    Reads a knownGene table from the UCSC Genome Browser.
    
    Specifications: this table has two lines, one of row headers and one
    of a single isoform of a gene.  The columns are specified by the UCSC
    genome browser.  See the schema here:
    http://genome.ucsc.edu/cgi-bin/hgTables and click "describe table schema"

    Input: a file name, including the directory name.
    Outputs three things:
     exonStarts - a list of exon starting points
     intronStarts - a list of intron starting points
     strand - a string that is either '+' or '-'.

    Example: readTable('datafiles/testPositiveStrand-exon-info.txt')
    returns [[3, 19], [9, 28], '+'].
    Usage: exonStarts,intronStarts,strand = readTable('datafiles/testPositiveStrand-exon-info.txt')
    
    '''
    # Read and parse the elements in the row.
    tableLines = open(infile,'r').readlines()
    row = tableLines[1].split()
    strand = row[2]
    transcriptionStart = int(row[3])  # convert the string to an int
    transcriptionEnd = int(row[4])
    codingRegionStart = int(row[5])
    codingRegionEnd = int(row[6])
    exonStarts = [int(start) for start in row[8].split(',') if len(start) != 0]
    intronStarts = [int(start) for start in row[9].split(',') if len(start) != 0]

    ## The variables now have the original values from the table.  We need
    ## to transform them by (1) moving indices of the non-coding portions
    ## of exons and (2) adjusting the indices to they start at 0.

    ## First, identify the positions of the coding regions.
    ## Sometimes entire exons are non-coding!  Remove these.
    indicesAbove5PrimeUTR = [i for i in range(len(intronStarts)) if intronStarts[i]>codingRegionStart]
    indicesBelow3PrimeUTR = [i for i in range(len(exonStarts)) if exonStarts[i]<codingRegionEnd]
    indicesToKeep = [i for i in range(len(exonStarts)) if i in indicesAbove5PrimeUTR and i in indicesBelow3PrimeUTR]
    exonStarts = [exonStarts[i] for i in indicesToKeep]
    intronStarts = [intronStarts[i] for i in indicesToKeep]

    ## the exonStarts and intronStarts must be adjusted to be coding regions only.
    ## We can now adjust the start point of the first exon and the end point
    ## of the last exon.
    if codingRegionStart > transcriptionStart:
        exonStarts[0] = codingRegionStart
    if transcriptionEnd > codingRegionEnd:
        intronStarts[-1] = codingRegionEnd

    # Print the number of exons, if we have completely removed some.
    #if len(exonStarts) != int(row[7]):
    #    print('After removing non-coding exons, %d exons left.' % (len(exonStarts)))

    ## shift the exon Starts and Ends to be 0.
    exonStarts = [start-transcriptionStart for start in exonStarts]
    intronStarts = [start-transcriptionStart for start in intronStarts]
 
    ## return the exonStarts and the intronStarts (indexed at 0)
    ## and the strand (+/-)
    return exonStarts,intronStarts,strand

def readFasta(infile):
    '''
    Returns the sequences in the FASTA file, with the line breaks (newlines)
    removed.

    Specifications: this file must have THREE sequences, labeled by three headers 
    named '>dna','>rna','>peptide'.

    Input: a file name, including the directory name.
    Output: three strings representing the DNA, RNA, and peptide sequencs.
    Example: readFasta('testPos') 
    '''

    ## fileLines is a list of strings from the infile variable.
    fileLines = open(infile,'r').readlines()

    ## dna, rna, and peptide will eventually contain the sequences
    ## we will return.
    dna = ''
    rna = ''
    peptide = ''

    ## thisheader will contain the most recent header (line with a ">").
    thisheader = '' 

    ## go through each line in fileLines...
    for line in fileLines:

        ## remove newlines
        strippedLine = line.strip()

        ## update the header if this line starts with a ">"
        ## otherwise, add the line to either dna, rna, or peptide.
        if strippedLine[0] == '>':
            thisheader = strippedLine
        else:
            ## make line upper case
            strippedLine = strippedLine.upper()

            ## check the header to see which variable to add the string to.
            if thisheader == '>dna':
                dna = dna + strippedLine
            elif thisheader == '>rna':
                rna = rna + strippedLine
            elif thisheader == '>peptide':
                peptide = peptide + strippedLine
            else:
                ## The header wasn't one of the ones above - print an error message.
                sys.exit('Error!  Header "'+thisheader+'" is not >dna, >rna, or >peptide. Exiting.\n')
    return dna,rna,peptide
