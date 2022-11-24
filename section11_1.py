import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)

from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))


dictionary = defaultdict(lambda: 'doesnt exist in the dict', {'a':1, 'b':2})
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d) # a dictionary in python doesn't have a sense of order before version 3.7. But now it is ordered!!

from array import array

arr = array('i', [1,2,3])

print(arr[0]) # accessing an array as a list.

# Pros and Cons of libraries

# debugging 
# linting
# ide/ editor (emacs?)
# pdb

import pdb

def add(num1, num2):
	# print(num1, num2)
	pdb.set_trace()
	return num1+num2
	
add(4, 'hhkhads')
