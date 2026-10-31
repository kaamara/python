from datetime import datetime

user_input = input("enter your goal with a deadline seperated by colon\n")
input_list = user_input.split(":") ## list

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_day = datetime.today()
time_till = deadline_date - today_day


print(f"dear user Time reamining for your goal: {goal} is {time_till.days} days")

# 3;54;00