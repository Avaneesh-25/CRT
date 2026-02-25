''' bug is an error.
    Debugging is the process of finding and fixing bugs.'''

try:
    a = int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
   
   