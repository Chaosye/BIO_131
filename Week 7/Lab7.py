##Nick Egan
## Lab for 3/21/17

import graphspace_utils

def main():

	## practice working with dictionaries
	dictionaryPractice()
	test_graphspace('Nick-Egan')
	return # done with the main() function.

def dictionaryPractice():
	'''
	practice with dictionaries.  No inputs and no outputs (uses print statements instead).
	'''
	ThatCount = 0
	
	myStr = 'That Sam I am That Sam I am I do not like That Sam I am'
	text = myStr.split() ## list of strings 
	
	## part 1: count number of That's
	for i in range(len(text)):
		if text[i] == "That":
			ThatCount = ThatCount + 1
	
	## part 2: print statements.
	print("Text reads:", text)
	print("The number of times 'That' occurs in the string is:", ThatCount)
	
	## part 3: make word frequency dictionary.
	freq = {}
	for i in range(len(text)):
		if text[i] not in freq.keys():
			freq[text[i]] = 1
		else:
			freq[text[i]] = freq[text[i]] + 1
	print(freq)
	return # done with dictionaryPractice() function.


def test_graphspace(your_name):
	'''
	Test function to post a basic graph to GraphSpace.  View the graph here:
	http://ec2-52-41-252-78.us-west-2.compute.amazonaws.com/
	Login with username "compbio@reed.edu" and password "compbio"
	'''
	edge_list = [['Choose your own adventure:','You face a bridge troll!'],['You face a bridge troll!','Oh no!  You have been defeated!'],['Oh no!  You have been defeated!','Its all over!  Noooo!'],['Its all over!  Noooo!','...Game Over...'],['You face a bridge troll!','Argh!  Fight back!'],['Oh no!  You have been defeated!','Run away!'],['Run away!', 'Oh, you made it over the bridge.'],['Oh, you made it over the bridge.','Congratulations, you won!'],['Argh!  Fight back!','The bridge troll has been defeated!'],['The bridge troll has been defeated!','Congratulations, you won!']]  #shows a list of connections

	node_list = []  #empty node list
	for e in edge_list:
		if e[0] not in node_list:  #Creates nodes based on reading from the edge list, first node of a pair
			node_list = node_list + [e[0]]
		if e[1] not in node_list:  #Creates nodes based on the second node detected
			node_list = node_list + [e[1]]

	node_attrs = {}
	for n in node_list:
		node_attrs[n] = {}
		node_attrs[n]['background_color'] = '#FFBD33'
	node_attrs['Choose your own adventure:']['background_color'] = '#75FF33'
	node_attrs['...Game Over...']['background_color'] = '#BD33FF'
	
	print(node_attrs)
	
	graphspace_utils.postBio131Graph(edge_list,node_attrs,your_name+'-test')
	print('Done!')
	return # done with test_graphspace() function.



## keep these lines at the bottom of the file.
if __name__ == '__main__':
	main()