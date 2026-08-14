calculation_to_units = 24
name_of_unit = "hours"

def days_to_unit(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "you entered a 0, please enter a positive integer!"

def validateandexecute():
    if u_input.isdigit():
        user_input_number = int(u_input)
        calculated_value = days_to_unit(user_input_number)
        print(calculated_value)
    else:
        print("your input is not a int number.")

u_input = input("Hey user, enter a number of days and i will convert it to hours\n")
validateandexecute()
