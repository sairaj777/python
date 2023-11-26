week = ["tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday" ]

def daycalculator(date):
    remainder = date % 7
    dates = range(7)
    week_dictionary = dict(zip(dates, week))
    return week_dictionary[remainder]
