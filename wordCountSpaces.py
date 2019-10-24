import re;
import string;

def wordCountSpaces(cswString, textList):

    # split gap phrase by word
    cswByWord = cswString.split();

    temp = re.findall(r'\d+', cswByWord[1])
    res = list(map(int, temp))

    # set up as list of lists: first list is range of distance between words,
    # second list is the words themselves
    codeSpacePhrase = [res, [cswByWord[0], cswByWord[2]]];

    sNum = res[0];                  # start gap number
    eNum = res[1];                  # end gap number
    phraseDist = res[1] - res[0];   # distance between gap numbers
    sWord = cswByWord[0];           # starting word
    eWord = cswByWord[2];           # ending word

    gapPhraseCount = 0;             # total amount of gap phrase found
    foundFlag = False;              # flag to raise if sWord found
    foundPos = -1;                  # position of sWord in textList

    for i in range(len(textList)):

        # if we find sWord, raise flag and note position.
        if textList[i] == sWord:
            foundFlag = True;
            foundPos = i;
            print(f"{sWord} found at pos {i}");
        if textList[i] == eWord:
            if foundFlag == True and i-foundPos<=phraseDist:
                print(f"{eWord} found at pos {i}");
                gapPhraseCount += 1;

    return gapPhraseCount;

# testing
# testList = ["Trials and mother fucking tribulations. There is nothing here but trials and tribulations. Did I say trials, tribulations? You can suck my trials, and also my god damn tribulations. Trials have no respect for the amounts of tribulations we have. Can you decide between trials and tribulations? Do trials, nay, tribulations have a difference?"]
# wordArray = [word for line in testList for word in line.split()]
# for i in range(len(wordArray)):
#     wordArray[i] = wordArray[i].translate(str.maketrans('', '', string.punctuation))
#     wordArray[i] = ''.join(filter(lambda x: x in string.printable, wordArray[i]))
#     wordArray[i] = wordArray[i].lower();
# print(wordArray);
# print(wordCountSpaces("trials [1<=w<=5] tribulations", wordArray));
