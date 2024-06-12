import calendar

month = int(input("Enter Month: "))
year = int(input("Enter Year: "))

cal = calendar.TextCalendar(calendar.MONDAY)

calendar_text = cal.formatmonth(year, month)
print(calendar_text)