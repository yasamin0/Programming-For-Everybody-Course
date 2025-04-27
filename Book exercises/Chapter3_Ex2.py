#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
#Example 1:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Example 2:
#Enter Hours: forty
#Error, please enter numeric input

try:
    hours = float(input("Enter Hours: ")) #I used float instead of int to allow decimal values for hours worked.
    rate = float(input("Enter Rate: "))
    if hours > 40:
        overtime = hours - 40
        gross_pay = (40 * rate) + (overtime * rate * 1.5) #Calculate pay for first 40 hours and add overtime pay
    else:
        gross_pay = hours * rate 

    print("Gross Pay: " ,  gross_pay)


except ValueError:
    print("Error, please enter numeric input")