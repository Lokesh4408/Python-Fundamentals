# List Methods
basket = [1,2,3,4,5]

# adding
basket.append(100) 
basket.insert(5, 200)
basket.extend([100, 101])
new_list = basket
print(basket)
print(new_list)

# removing
new_list = basket.pop()
basket.pop(0)
basket.remove(4)
basket.clear()
print(basket)
print(new_list)

basket = ['a','b','c','d','e', 'd']
print('d' in basket)
print('i' in 'hi your are late')
print(basket.index('b'))
print(basket.count('d'))
basket.sort()
new_basket = basket.copy()
print(sorted(basket)) # creates a new basket and sorts it without altering the original basket.
print(new_basket)
basket.reverse()
print(basket)

# Common list patterns
basket = ['a','x', 'b','c','d','e', 'd']
basket.sort()
basket.reverse()
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Lokesh'])
new_sentence2 = '   '.join(['still', 'the', 'same', 'string'])
print(new_sentence)
print(new_sentence2)
print(basket[::-1]) # this just creates a new list without altering the original
print(basket)
print(list(range(101)))

