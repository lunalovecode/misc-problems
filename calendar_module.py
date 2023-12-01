import calendar
m, d, y = [int(x) for x in input().split()]
print(["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"][calendar.weekday(y, m, d)])