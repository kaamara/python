def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
       return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a positive integer!")
        else:
            print("you entered a negative, please enter a positive integer!")
    except ValueError:
        print("your input is not a int number.")

user_input_message = "Hey user, enter number of days and conversion unit!\n"