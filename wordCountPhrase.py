import re;
import string;

def wordCountSpaces(subString, textList):

    # split gap phrase by word
    searchPhraseList = subString.split();

    # set up as list of lists: first list is range of distance between words,
    # second list is the words themselves

    phraseLen = len(searchPhraseList);


    phraseCount = 0;                # total amount of gap phrase found
    foundFlag = False;              # flag to raise if sWord found
    foundPos = -1;                  # position of sWord in textList


    for i in range(len(textList)):

        if textList[i] == searchPhraseList[0]:
            foundFlag = True;
            foundPos = i;
            # print(f"{searchPhraseList[0]} found at pos {i}");
            for j in range(len(searchPhraseList)):
                print(f"spl:{searchPhraseList[j]} txt:{textList[foundPos+j]}")
                if searchPhraseList[j] != textList[foundPos+j]:
                    print("Different! Breaking.");
                    foundFlag = False;
                    break;
            if foundFlag == True:
                phraseCount += 1;
            foundFlag = False;

    return phraseCount;

# testing
# testPhrase = "trials and";
# testList = ["Trials and mother fucking tribulations. There is nothing here but trials and tribulations. Did I say trials, tribulations? You can suck my trials, and also my god damn tribulations. Trials have no respect for the amounts of tribulations we have. Can you decide between trials and tribulations? Do trials, nay, tribulations have a difference?"]
# wordArray = [word for line in testList for word in line.split()]
# for i in range(len(wordArray)):
#     wordArray[i] = wordArray[i].translate(str.maketrans('', '', string.punctuation))
#     wordArray[i] = ''.join(filter(lambda x: x in string.printable, wordArray[i]))
#     wordArray[i] = wordArray[i].lower();
# print(wordArray);
# print(wordCountSpaces(testPhrase, wordArray));
