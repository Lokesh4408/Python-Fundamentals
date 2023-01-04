
    
'''try:
    with open('test.txt', mode='r+') as my_file: # r,w,a
        text = my_file.write('hey it\'s my info for the future')
        # print(my_file.readlines())
        print(text)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err'''
    
# Exercise: Translator
from translate import Translator

translator = Translator(to_lang="zh")
text = "This is a pencil."
translation = translator.translate(text)
print(f'In chinese: {translation}- {text}')