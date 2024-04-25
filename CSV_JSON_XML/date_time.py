from datetime import date, time, datetime, timedelta
import pytz

#Get current date and time
print(f'Currnet date and time is {datetime.now()}')

#Date Time Arithmetic
print(f'The future date after 7 days is {datetime.now()+timedelta(days = 7)}')

# Parameters for timedeltas
# days, seconds, microseconds, milliseconds, minutes, hours, weeks
print(f'The date before 2 weeks and 2 days is {datetime.now()-timedelta(weeks = 2, days =2)}')

#Formatting of date and time

# strftime
# parameters for strftime
# %a %A weekday name (abbreviation, Full)
# %w weekdays as a decimal number
# %d days of the month
# %b %B month name (abbreviation, Full)
# %m Month as a decimal number 
# %y %Y years (2 digits, 4 digits)
# %H hours (24 hour clock)
# %I hours(12 hour clock)
# %p AM or PM 
# %M minutes (2 digits)
# %S seconds (2 digits)
# %f microseconds (00000-99999)
# %z %Z Timezone (+HHMM/ -HHMM or name)
# %j Day of the year
# %U %W week number of the year (First sunday of new year -0/ first monday of new year -1)

print(f"Formatted date is {datetime.now().strftime('%y-%m-%d')}")
print(f"Formatted date is {datetime.now().strftime('%d-%B-%y')}")
print(f"Formatted date is {datetime.now().strftime('%j')}")
print(f"Formatted date is {datetime.now().strftime('%a')}")
print(f"Formatted date is {datetime.now().strftime('%U')}")

print(f"Formatted date is {datetime.now().strftime('%H-%M-%S %p')}")
print(f"Formatted date is {datetime.now().strftime('%f')}")
# print(f"Time zone is {datetime.now().strftime('%Z')}")

easter = pytz.timezone('US/Eastern')
l_d=easter.localize(datetime.now())
print(f"localized Time is {l_d}")

#Parsing of time

# strptime - converts a properly formatted string to datetime and object
# parameters - same as strftime

s= '18 March, 2024'
print(f'Date string is {s} and its type is {type(s)}')
d=datetime.strptime(s, '%d %B, %Y')
print(f'Date string is {s} and its type is {type(d)}')

# Error
# s= '18 March, 2024'
# print(f'Date string is {s} and its type is {type(s)}')
# d=datetime.strptime(s, '%d %b, %Y')
# print(f'Date string is {s} and its type is {type(d)}')