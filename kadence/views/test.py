from datetime import date


today = str(date.today())

current_date = today.split("-")

current_year = int(current_date[0])
current_month = int(current_date[1])
current_day = int(current_date[2])

list_date = "1987-5-24"
new_list_date = list_date.split("-")

listed_year = int(new_list_date[0])
listed_month = int(new_list_date[1])
listed_day = int(new_list_date[2])

d0 = date(listed_year, listed_month, listed_day)
d1 = date(current_year, current_month, current_day)
total_days = d1 - d0
print(total_days.days)





















