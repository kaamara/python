calculation_to_units = 24
name_of_unit = "hours"

def days_to_unit(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validateandexecute():
    try:

        user_input_number = int(u_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a positive integer!")
        else:
            print("you entered a negative, please enter a positive integer!")
    except ValueError:
        print("your input is not a int number.")

u_input = ""
while u_input != "exit":
    u_input = input("Hey user, enter a number of days and i will convert it to hours\n")
    validateandexecute()

# 2;03;00