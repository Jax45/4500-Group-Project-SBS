# needed for filtering
import string;

#initializing list to hold text
wordArray = [];

# open file, and set wordArray as list of words in file without newlines
with open('testText.txt') as f:
    wordArray = [word for line in f for word in line.split()]

# filter out punctuation and unrecognizable characters, make lower case
for i in range(len(wordArray)):
    wordArray[i] = wordArray[i].translate(str.maketrans('', '', string.punctuation))
    wordArray[i] = ''.join(filter(lambda x: x in string.printable, wordArray[i]))
    wordArray[i] = wordArray[i].lower();
