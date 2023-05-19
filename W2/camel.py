# Get input from user
variable_name = input("camelCase: ")

print("snake_case: ", end='')

# Check every character in user's input for uppercase characters and convert them to lower case with "_" as prefix
for c in variable_name:
    if c.isupper():
        c = ("_" + c.lower())

    # Convert and print user's input as snake_case
    print(c, end='')
