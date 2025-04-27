#Write another program that prompts for a list of numbers like exercise 1 chapter 5 of book and at the end prints out both the maximum and minimum of the numbers instead of the average.

largest = None
smallest = None

while True:
    inp = input("Enter a number: ")
    if inp.lower() == "done":
        break
    try:
        num = float(inp)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")

if largest is not None and smallest is not None:
    print("Maximum:", largest, "Minimum:", smallest)
else:
    print("No valid numbers entered")