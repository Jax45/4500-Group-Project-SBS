# needed for filtering
import string;
import re;

# opening test codebook file
with open('testCodebook.txt') as f:
    cbLines = f.readlines();
cbLines = [x.strip() for x in cbLines];
f.close();

# searchables from codebook
# word, phrase, and phrase with spaces.
codeWord        = cbLines[0];
codePhrase      = cbLines[1];
codeTemp        = cbLines[2].split();

temp = re.findall(r'\d+', codeTemp[1])
res = list(map(int, temp))

# set up as list of lists: first list is range of distance between words,
# second list is the words themselves
codeSpacePhrase = [res, [codeTemp[0], codeTemp[2]]];
print(codeSpacePhrase);

#initializing list to hold text
wordArray = [];

# open file, and set wordArray as list of words in file without newlines
with open('testText.txt') as f:
    wordArray = [word for line in f for word in line.split()]
f.close();

# filter out punctuation and unrecognizable characters, make lower case
for i in range(len(wordArray)):
    wordArray[i] = wordArray[i].translate(str.maketrans('', '', string.punctuation))
    wordArray[i] = ''.join(filter(lambda x: x in string.printable, wordArray[i]))
    wordArray[i] = wordArray[i].lower();
