# Task:  Loop though days of a month and print Friyay when the day is Friday. From Wed to Thrusday you need to print 'Almost there 🙂'


from functions import *
from class_file import Car
from random import choice

lancer = Car("lancer","mistibushi",2016)
jazz = Car("jazz","honda",2004)
swift = Car("swift","maruthi",2011)

print(__name__)

if (__name__ == "__main__" ):
    date = int(input ("Enter the date of the month: ")) #date variable
    day = str(daycalculator(date))                       #calling the dayCalculator function form functions file
    car_model = choice(list(Car.car_dict.keys()))
    print(day.lower())
    if (day.lower() == "monday"  or day.lower() == "tuesday"):
        print ("its the start of the week and you can drive: ", car_model)
    elif (day.lower() == "wednesday" or day.lower() == "thursday"):
        print ("almost there ! and you can drive: ", car_model)
    elif (day.lower() == "friday"):
        print ("its friday !! and you can drive: ", car_model)
    else:
        print ("its weekend !!! and you can drive: ", car_model)

















