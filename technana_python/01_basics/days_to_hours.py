from encodings import utf_8

calculation_to_units = 24
name_of_unit = "hours"

def days_to_unit(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_number = int(u_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a positive integer")
        else:
            print("you entered a negative number")
    except ValueError:
        print("your input is not a number. Please enter a integer")


u_input = "" #1. assing an empty value to u_input
while u_input != "exit": #2. condition gets evaluated
    u_input = input("Hey user, enter a number of days and i will convert it to hours\n") #3. User is prompted for its input
    validate_and_execute() #4. Function is called and input is validated and executed
# 5. Second loop: check if "exit" was typed

