## HW3 Out Feb 6
## HW3 Due Feb 17
## HW3.1 internal deadline: Feb 10
## HW3.2 internal deadline: Feb 13

## NAME:
## ESTIMATED TIME:

## This line "reads" anna_challenge_functions.py and loads some functions that Anna has written.
import anna_challenge_functions

def main():
    '''
    This main() function converts the DNA sequence from a dataset into mRNA and 
    finally to a peptide sequence.
    Inputs: Nothing (set dataset variable below)
    Outputs: Nothing.
    '''

    # Set dataset to one of the following strings: 'testPos','SRC','testNeg', or 'TMPRSS2'
    dataset = 'testPos'
    print('Dataset:',dataset)

    # Use the getData() function from anna_functions.py to get all the information
    # associated with a dataset.
    dna,exonStarts,intronStarts,strand,rnaFromFile,peptideFromFile = anna_challenge_functions.getData(dataset)

    # CALL FUNCTIONS WITHIN MAIN() HERE.  
    
    return # done with the main() function.

    # WRITE NEW FUNCTIONS HERE.

## The lines below will call the main() function 
if __name__ == '__main__':
    main()
