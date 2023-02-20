
# An Empty list that can store inputs from user
the_list = []
# A loop for multiple inputs from user
while True:
    input_string = input("Enter an integer or Type 'done' to exit: ")

    # A check if the user wants to end
    if input_string == "done":
        break

    # Adding user inputs to the list

    # Checking if the user input is integer or not
    if input_string.isdigit():
        the_list.append(int(input_string))
    else:
        print("Invalid input. Please enter an integer.")
the_list.sort()
print(f"The sorted list is {the_list}\n")
added_number = input("Enter any number in the list: ")
# Enter another number
the_list.append(int(added_number))
the_list.sort()
print(the_list)

