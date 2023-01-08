# Regular Expressions
import re

pattern = re.compile('of')
string = 'search inside of this text please!'

print('search' in string)

a = re.search('this', string) # returns an object with span of the search word description & more.
b = pattern.search(string) # pattern.findall(string), pattern.fullmatch(string), pattern.match(string).
print(a.span())
print(a.group())
print(b.span())

# At least 8 char long
# contains any sort of letters, numbers $%#@
# has to end with a number
pattern2 = re.compile(r"[A-Za-z0-9%$#@]{8,}\d")
password = 'skdfjsadfkj$d%89'
check = pattern2.fullmatch(password)
print(check)

def do_stuff(num):
    try:
        return num + 5
    except TypeError as err:
        return err