import time
import datetime

current_time = datetime.datetime.now()
current_hour = current_time.strftime("%H")

# print(current_time)
print(current_hour)

while current_hour == "18" or current_hour == "19" or current_hour == "20" or current_hour == "21" or current_hour == "22" or current_hour == "23" or current_hour == "00" or current_hour == "01" or current_hour == "02" or current_hour == "03":
    print(current_time)
    print(current_hour)

    # re-check the time
    current_time = datetime.datetime.now()
    current_hour = current_time.strftime("%H")

print('should not run')