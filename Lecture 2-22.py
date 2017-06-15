#Lecture 2/22/17
#Nick Egan
#Manipulating Files

fname = 'mysteryFile.txt'
myFile = open(fname, 'r')
text = myFile.read()
myFile.close()
#strip() has a special syntax of 'String'.strip and clears out whitespace on the ends of strings.
text = text.strip()
#text = '\n'.join(text) #inputting a string converts a string into a list and then back into a string.
#text = text.split('.')
text = text.split('\n')
text = ' about that doggo. \n'.join(text)
text = text.split('.')
text = ', '.join(text)
print(text)



#to make 'bacadae' into [b,c,d,e], split by a particular letter, in this case an 'a'.  You can also join them together with an'a'!
#split() and join()
#text.split('a') splits a string text by the character a
#'a'.join(['a','b'])