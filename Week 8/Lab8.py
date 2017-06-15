##Nick Egan
##Lab 8: Make Patterns in Tables
##3/28/17
#Citations:
# List copying function list() from https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
# NEED TO FIX INITIALIZER - SWAPPED ROWS/COLUMNS

def main():

	inittable = initialize_table(5, 5)
	pattern1(inittable)
	pattern2(5)
	LSC("ATGTTATA","ATCGTCC")
	
	return
	
def printTable(table):
	for row in range(len(table)):
		print(table[row])
	print('')
	return
	
def initialize_table(ncols, nrows):
	##Input: two integers, the number of rows and columns
	##Output: nrows by ncols table (list of lists) filled with 0'seek
	
	tablecol = []
	table = []
	
	#Makes a row of 0's, ncols being the number of columns in the table
	
	
	#Stacks rows of 0's, nrows being the number of rows in the table
	for i in range(nrows):
		tablecol = []
		for j in range(ncols):
			tablecol.append(0)
		table.append(tablecol)
	
	#prints the table
	#printTable(table) #DB
	
	return table
	
def pattern1(inittable):
	
	table = inittable
	
	for i in range(len(table)):
		for j in range(len(table[0])):
			if i == 0 or j == 0:
				table[i][j] = 0
				
			elif i > 0 and j > 0:
				table[i][j] = table[i-1][j-1]+1
	
	#printTable(table)
		
	return
	
def pattern2(n):
	##Input: initialized table full of 0's
	##Output: fill a table where the first column is increasing by one, the last column is the maximum number, and the middle numbers increase by one every column.
	
	table = []
	
	#Initializes graph with 0's.
	for i in range(n):
		tablecol = []
		for j in range(n):
			tablecol.append(0)
		table.append(tablecol)
	
	for i in range(n):
		for j in range(n):
			if i > 0 and j == 0:
				table[i][j] = table[i-1][j]+1	
				
	for i in range(n):
		for j in range(n):
			if i == 0 and j > 0:
				table[i][j] = table[i][j-1]+1	
				
	for i in range(n):
		for j in range(n):
			if i > 0 and j > 0:
				table[i][j] = table[i-1][j-1]+1
	
	#printTable(table) #DB
	
	return

def LSC(string1, string2): #Compute the length of the longest common subsequence between two strings
	##Inputs: two string, string1 and string2
	##Outputs: The length of the longest common subsequence between string1 and string2
	
	table = []
	bestOption = 0
	holder = []
	
	table = initialize_table(len(string2)+1,len(string1)+1)
	#printTable(table)
	
	for i in range(len(string1)+1):
		for j in range(len(string2)+1):
			holder = [0]
			if i > 0:
				holder.append(table[i-1][j])
			if j > 0:
				holder.append(table[i][j-1])
			if i > 0 and j > 0:
				if string1[i-1] == string2[j-1]:
					holder.append(table[i-1][j-1]+1)
				else:
					holder.append(table[i][j])
			#print(i,j,holder)
			table[i][j] = max(holder)
	printTable(table)
	return 
	
if __name__ == '__main__':
	main()