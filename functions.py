import math

#Function to validate an age as a positive integer, raises a ValueError if not a positive integer
def validate_age(age):
    #Takes a parameter and determines whether it is a positive integer or not
    if age <= 0:
        #If not raises a ValueError indicating as much, if this exception is caught ensure the age parameter is a positive integer
        raise ValueError("Age cannot be a negative number or Zero.")
    else:
        #If age IS a positive integer, returns age
        return age
    
#Function to calculate area of a rectangle    
def calculate_rectangle_area(length, width):
    return length * width

#Function to calculate area of a circle
def calculate_circle_area(radius):
    return math.pi * (math.pow(radius,2))

#Fucntion to calculate area of a given shape based on parameters passed
def get_area(shape, *args):
    #Checks shape
    if shape.lower() == "rectangle":
        #Sets length and width to the parameters passed
        length = args[0]
        width = args[1]
        #Calls the calclulate_rectangle_area function passes the appropriate parameters
        return calculate_rectangle_area(length,width)
    #Checks shape
    elif shape.lower() == "circle":
        #Sets radius to the parameter passed
        radius = args[0]
        #Calls the calculate_circle_area function and passes the radius as it's parameter
        return calculate_circle_area(radius)
