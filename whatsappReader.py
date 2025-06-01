# Python program to read
# file word by word
count = 0

# opening the text file
with open('C:\\Users\\ivanr\\Downloads\\WhatsappChatWithLenaTill2ndJuly\\WhatsAppChatWithLena.txt', 'r', encoding='utf-8') as file:

    # reading each line
    for line in file:

        #for reading each word
        for word in line.split():

            #displaying the words
            #print(word)
            if word=='love':
                count+=1
print('Total number of times we said love to eachother till 2nd July 2024: ', count)