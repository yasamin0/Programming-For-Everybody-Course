#Write a program to prompt the user for hours and rate per hour to compute gross pay. 

hours = float(input("Enter Hours: ")) #I used float instead of int to allow decimal values for hours worked.
rate = float(input("Enter Rate: "))
gross_pay = hours * rate 
print("Gross Pay: " ,  gross_pay)