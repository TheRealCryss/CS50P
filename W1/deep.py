great_question = input("What is the answer to the Great Question ...\n")

# Convert to lower case for the task's requirement of being case insensitive
# casefold is used instead of lower as it is the better option for comparisions

if great_question.strip(" ").casefold() in ["42", "forty-two", "forty two"]:
    print("Yes")

else:
    print("No")
