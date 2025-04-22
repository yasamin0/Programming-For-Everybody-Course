#Write a program that prompts the user for a Celsius temperature, 
#converts the temperature to Fahrenheit, and prints out the converted temperature.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("Temperature in Fahrenheit:", fahrenheit)
