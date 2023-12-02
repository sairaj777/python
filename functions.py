import string
week = ["tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday" ]

def daycalculator(date):
    remainder = date % 7
    dates = range(7)
    week_dictionary = dict(zip(dates, week))
    return week_dictionary[remainder]

def duplicateTestor(importedString): # function to test  duplicate letters in words
    for words in importedString:
        if len(words) > len(set(words)):
            return True
            break
    else:
        return False


def shadowSentenceTest(sentence1,sentence2): # function to test shadow sentences
    if (len(sentence1) == len(sentence2)):
        for index, word in enumerate(sentence1):
            if len(set(sentence1[index]).intersection(set(sentence2[index]))) > 1:
                return False
                break
            else:
                return True
    else:
        return False



