# Task:  Loop though days of a month and print Friyay when the day is Friday. From Wed to Thrusday you need to print 'Almost there 🙂'
from functions import *
from class_file import Car
from random import choice
import socket
import datetime

# find dns from ip address

hostname = socket.gethostbyaddr(input("provide the ip address: "))[0]
print (f"the host name is {hostname}")

# task task to find duplicate letters in words

current_datetime = datetime.datetime.now()
duplicateString =duplicateTestor( list(input("enter the string: ").split())) # importing the sentence to test duplicates
#print (duplicateString)

file = open("File_Duplicate_String",'a')
file.write(f"{current_datetime}: {str(duplicateString)}\n")

# Shadow sentence task

sentence1 = list(input("enter the 1st sentence: ").split())
sentence2 = list(input("enter the 2nd sentence: ").split())
shadowSentence = shadowSentenceTest(sentence1, sentence2)
print(f"the sentences are shadow sentence: {shadowSentence}")

# Car task

lancer = Car("lancer","mistibushi",2016)
jazz = Car("jazz","honda",2004)
swift = Car("swift","maruthi",2011)

if (__name__ == "__main__" ):
    date = int(input ("Enter the date of the month: ")) #date variable
    day = str(daycalculator(date))                       #calling the dayCalculator function form functions file
    car_model = choice(list(Car.car_dict.keys()))
    if (day.lower() == "monday"  or day.lower() == "tuesday"):
        print ("its the start of the week and you can drive: ", car_model)
    elif (day.lower() == "wednesday" or day.lower() == "thursday"):
        print ("almost there ! and you can drive: ", car_model)
    elif (day.lower() == "friday"):
        print ("its friday !! and you can drive: ", car_model)
    else:
        print (f"the day is {day} and its weekend !!! and you can drive: ", car_model)


















