import random
import string
import datetime
import math

def gen_random_pw(length):
    #Check password length
    if length < 8:
        return print("Password length must be 8 characters or more.")
    #Instance password variable so it can be used later in while loop
    password = ''
    #Make a list of valid characters from lists found in the string module
    valid_characters = string.ascii_letters + string.digits
    #Adds a random character from valid_characters for the entire given length of the password provided by parameter length
    while length > 0:
        password += random.choice(valid_characters)
        length -= 1
    return password

def get_date_difference(date1, date2):
    #Make date objects given the two date strings from input parameters
    day1 = datetime.date.fromisoformat(date1)
    day2 = datetime.date.fromisoformat(date2)
    #Make an integer that represents the number of days between the two dates
    day_diff = abs(day1 - day2)
    return(day_diff.days)

def circle_area(radius):
    area = math.pi * (pow(radius, 2))
    return(area)
