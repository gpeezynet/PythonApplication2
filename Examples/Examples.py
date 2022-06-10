#
# Two sample answers for George
#

operation = input("Would you like to +, -, *, / numbers?: ")   # Ask what the user wants to do
first = float(input("first number: "))                         # Get the frist number from the user
second = float(input("second number: "))                       # Get the second number from the user

# One way is to use "if-elif-else" statements, "elif" is short for "else if"
print("Using if statements...")
if operation == "+":
   print(float(first) + float(second))
elif operation == "-":
   print(float(first) - float(second))
elif operation == "*":
   print(float(first) * float(second))
elif operation == "/":
   print(float(first) / float(second))
else:
   print("You chose and invalid operation")

# Another way is to use match (called 'switch' in C#)
print("Using a match statement...")
match operation:
   case "+":
      print(float(first) + float(second))
   case "-":
      print(float(first) - float(second))
   case "*":
      print(float(first) * float(second))
   case "/":
      print(float(first) / float(second))
   case default:
      print("You chose and invalid operation")
   