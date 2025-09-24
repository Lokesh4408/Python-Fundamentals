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
