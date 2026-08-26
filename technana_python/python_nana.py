
def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
       return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

def validateandexecute():
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

u_input = ""
while u_input != "exit":
    u_input = input("Hey user, enter a number of days and conversion unit\n")
    days_and_unit = u_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validateandexecute()

    #3;01;43


message = "enter some value"
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days_ = [20, 40, 20, 100]
list_of_months = ["January", "February", "March", "April"]
set_of_days = {20, 45, 100}
days_and_unit = {"days": 10, "unit": "hours"}