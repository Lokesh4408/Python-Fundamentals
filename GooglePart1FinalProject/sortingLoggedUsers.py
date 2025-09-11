numbers= [4, 6, 2, 7, 1]
numbers.sort()
print("Sorted numbers:", numbers)

names = ['Carlos', 'Ray', 'Alex', 'Kelly']
print(names)
print("Sorted names:", sorted(names))
print('Sorted names length wise:', sorted(names, key=len))
# sorted function returns a new sorted list, it does not modify the original list
# sort function sorts the list in place and returns None