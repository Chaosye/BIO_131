#Lab 2 - Pattern Maker Lab
#Nick Egan

#Begin making patterns ---
#Make a 5x5 rectangle

size = 1 # doesn't really work but it's cool at huge sizes!

for rect in range(6 * size):
	print('*****')
print()	
	
#Make a right triangle---
for righttriangle in ['*','**','***','****','*****']:
	print(righttriangle)
print()

#Make a play button-------
for playbutton in ['*','**','***','****','*****', '****', '***', '**', '*']:
	print(righttriangle)
print()

#Make another triangle-----
tristar = 0
trispace = 5 * size
for antriangle in range(5 * size):
	tristar = tristar + 1
	trispace = trispace - 1
	print(' ' * trispace + '*'*2*tristar)
print()	

#Make a diamond------------
distar = 0
dispace = 5 * size
for andiamond in range(5 * size):
	distar = distar + 1
	dispace = dispace - 1
	print(' ' * dispace + '*'*2*distar)
for andiamond in range(5 * size):
	print(' ' * dispace + '*'*2*distar)
	distar = distar + -1
	dispace = dispace + 1
print()

#Make a rectangle outline---
fivestar = '*****'
print(fivestar)
for rectoutline in range(3 * size):
	print('*   *')
print(fivestar)
print()

#Make a diamond outline-----
dioutspace = 0
dioutbackspace = 5 * size
for dioutline in range(5 * size):
	print(' ' * dioutbackspace + '*' + ' ' * 2 * dioutspace + '*')
	dioutspace = dioutspace + 1
	dioutbackspace = dioutbackspace - 1
for dioutline in range(6 * size):
	print(' ' * dioutbackspace + '*' + ' ' * 2 * dioutspace + '*')
	dioutspace = dioutspace - 1
	dioutbackspace = dioutbackspace + 1
print()





