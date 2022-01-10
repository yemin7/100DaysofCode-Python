leap = False
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap = True
      else:
        leap = False
    else:
      leap = True
  else:
    leap = False
  return leap

def days_in_month(f_year, f_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(f_year) and month == 2:
    return 29
  return month_days[f_month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)