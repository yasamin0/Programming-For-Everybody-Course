# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
# Example shown:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        gross_pay = (40 * rate) + (overtime * rate * 1.5) #Calculate pay for first 40 hours and add overtime pay
    else:
        gross_pay = hours * rate 
    return gross_pay

try:
    hours = float(input("Enter Hours: ")) #I used float instead of int to allow decimal values for hours worked.
    rate = float(input("Enter Rate: "))
    pay = computepay(hours, rate) #Call the function to compute pay
    print("Gross Pay: " ,  pay)

except ValueError:
    print("Error, please enter numeric input")