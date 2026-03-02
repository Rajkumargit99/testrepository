from datetime import datetime

current_date = datetime.now()
#print(current_date) # 2026-03-01 17:17:40.820521

print("date:", current_date.date())
print("week:", current_date.weekday())
print("month:", current_date.month)
print("year:", current_date.year)
print("hour:", current_date.hour)
print("min:", current_date.minute)
print("day:", current_date.day)
print("-----------")
# date formatting

date_time_format = current_date.strftime("%d %m %b %y %Y %H %M %S")
print(date_time_format)

print("-----------")

print("2 days ago: ", (current_date+timedelta(days=2)).date())
