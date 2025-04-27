#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
 
hours = float(input("Enter Hours: ")) #I used float instead of int to allow decimal values for hours worked.
rate = float(input("Enter Rate: "))
if hours > 40:
    overtime = hours - 40
    gross_pay = (40 * rate) + (overtime * rate * 1.5) #Calculate pay for first 40 hours and add overtime pay
else:
    gross_pay = hours * rate 

print("Gross Pay: " ,  gross_pay)