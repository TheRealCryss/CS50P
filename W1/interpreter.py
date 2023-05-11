# Calculate input expression (Format: "x y z". Example "1 / 7")
#
expression = input("Expression: ")
x, y, z = expression.split()

x = float(x)
z = float(z)

if (y == "/" and z == "0"):
    print("Division by zero!")
elif y == "+":
    result_1 = x + z
    print(result_1)
elif y == "-":
    result_2 = x - z
    print(result_2)
elif y == "*":
    result_3 = x * z
    print(round(result_3,1))
elif y == "/":
    result_4 = x / z
    print(round(result_4,1))

"""
# Nicer solution with match
# Get the expression
x , y , z = input("Expression: ").strip().split()

# Change type of variable x and z
x = float(x)
z = float(z)

 Perform the operations
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        print(x / z)
    case "*":
        print(x * z)
"""