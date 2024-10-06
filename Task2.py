import math

def fraction_result(numerator,denominator):
    try:
        return numerator//denominator
    except:
        return math.inf

    



numerator=float (input("Enter the numrator of the fraction:\n"))
denominator=float (input("Enter the of denominator the fraction:\n"))


print ("the result is :\n",fraction_result(numerator,denominator))