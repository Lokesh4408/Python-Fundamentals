# List Methods
basket = [1, 2, 3, 4, 5]

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

basket = ['a', 'b', 'c', 'd', 'e', 'd']
print('d' in basket)
print('i' in 'hi your are late')
print(basket.index('b'))
print(basket.count('d'))
basket.sort()
new_basket = basket.copy()
# creates a new basket and sorts it without altering the original basket.
print(sorted(basket))
print(new_basket)
basket.reverse()
print(basket)

# Common list patterns
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Lokesh'])
new_sentence2 = '   '.join(['still', 'the', 'same', 'string'])
print(new_sentence)
print(new_sentence2)
# this just creates a new list without altering the original
print(basket[::-1])
print(basket)
print(list(range(101)))

# List unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(other)
print(d)

# None
weapons = None

# Dictionary: it is a datatype and also data structure
dictionary = {
    'a': [1, 3, 4],
    'b': 'hello',
    'x': True
}

my_list = [{
    'a': [1, 3, 4],
    'b': 'hello',
    'x': True
},
    {
    'a': [5, 6, 7],
    'b': 'hello',
    'x': True
}]

print(my_list[0]['a'][2])
print(dictionary)

# dictionaries are better than lists when you want to have more information stored.
# dictionary keys are supposed to be immutable. A key in a dictionary has to be unique.

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 23
}
print(user.get('age'))
user2 = dict(name='Lokesh')  # using built-in function dict.
# 55 is printed as default incase 'age' key is not available in dictionary.
print(user.get('cow', 55))
print(user2)
print('hello' in user.values())

print(user.items())
user2 = user.copy()
print(user.clear())
print(user)
print(user2)

print(user2.pop('age'))
# print(user.popitem()) : this removes the last key:value pair that was inserted into the dictionary.
print(user2.update({'age': 55}))
print(user2)


# Tuples: 3rd data structure, these are immutable.
my_tuple = (1, 2, 3, 4, 5, 5)
print(my_tuple[2])
print(5 in my_tuple)
print(user2.items())

new_tuple = my_tuple
print(new_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))


# Sets: Set is an unordered collection of unique objects
my_set = {1, 2, 3, 4, 5, 5, 6, 6}
my_set.add(100)
my_set.add(2)
print(my_set)

# return only unique items from the below list
my_list = [1, 2, 3, 4, 5, 5]
set1 = set(my_list)
new_set = my_set.copy()
print(set1)
print(len(set1))
my_set.clear()
print(list(new_set))
print(my_set)

# Methods in Sets
my_set = {1, 2, 3, 4, 5, 6}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))
print(my_set.discard(5))
print(my_set)
my_set.difference_update(your_set)
print(my_set)
print(my_set.intersection(your_set))
print(my_set & your_set)
print(my_set.isdisjoint(your_set))
print(my_set.union(your_set))
print(my_set | your_set)

print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))
