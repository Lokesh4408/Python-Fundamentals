guests = open('novel.txt', 'w')
initial_guests = ['Bob', 'Andrea', 'Manuel', 'Polly', 'Khalid']

for i in initial_guests:
    guests.write(i + '\n')

guests.close()

with open('novel.txt') as guests:
    for line in guests:
        print(line.strip())

new_guests = ['Sam', 'Danielle', 'Jacob']
with open('novel.txt', 'a') as guests:
    for i in new_guests:
        guests.write(i + '\n')

guests.close()

with open('novel.txt') as guests:
    for line in guests:
        print(line.strip())

#removing guests who already checked out.
checked_out = ['Andrea', 'Manuel', 'Khalid']
temp_list = []
with open('novel.txt', 'r') as guests:
    for g in guests:
        temp_list.append(g.strip())

with open('novel.txt', 'w') as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + '\n')

#checking who is still in the hotel
with open('novel.txt') as guests:
    for line in guests:
        print(line.strip())

# Verifying if the checked out guests are removed
guests_to_check = ['Bob','Andrea']
checked_in = []

with open('novel.txt') as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print('{} is checked in'.format(check))
        else:
            print('{} has already checked out'.format(check))
