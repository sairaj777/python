week = ["tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday" ]

def daycalculator(date):
    remainder = date % 7
    dates = range(7)
    week_dictionary = dict(zip(dates, week))
    return week_dictionary[remainder]
def duplicateTestor(importedString):               # function to test sentence duplicates
    if (len(importedString) == len(set(importedString))):
        return False
    else:
        return True


