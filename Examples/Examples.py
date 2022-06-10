operation = input("Would you like to +, -, *, / numbers?: ")
first = float(input("first number: "))
second = float(input("second number: "))

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

print("Using a match (or 'switch') statement...")
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
   