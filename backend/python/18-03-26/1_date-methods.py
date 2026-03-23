#date methods: datetime, date, time, timedelta

from datetime import datetime, date, time, timedelta
#datetime
now = datetime.now()
print(f"Current Date and Time: {now}")

#dateA
today = date.today()
print(f"Today's Date: {today}")

#time
current_time = time(14, 30, 45)
print(f"Current Time: {current_time}")

#timedelta
delta = timedelta(days=5, hours=3)
print(f"Time Delta: {delta}")

#utc time-utc.now()
print(f"UTC Time: {datetime.utcnow()}")

#datetime to string(year, month, day, hour, minute, second)
dob=datetime(1990, 5, 15)
# dob_str=dob.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Date of Birth (String): {dob_str}")
print(f"Date of Birth: {dob}")

#strftime = string to datetime
#strftime to datetime
# %A -Day in words Full weekday name
# %B -Month in words Full month name
# %a -Day in words Abbreviated weekday name
# %b -Month in words Abbreviated month name
# %d -Day of the month as a zero-padded decimal number
# %m -Month as a zero-padded decimal number
# %Y -Year with century as a decimal number
# %y -Year without century as a zero-padded decimal number
# %H -Hour (24-hour clock) as a zero-padded decimal number
# %I -Hour (12-hour clock) as a zero-padded decimal number
# %p -AM or PM
# %M -Minute as a zero-padded decimal number
# %S -Second as a zero-padded decimal number
# %f -Microsecond as a decimal number, zero-padded on the left
# %j -Day of the year as a zero-padded decimal number
# %U -Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number
# %W -Week number of the year (Monday as the first day of the week) as a zero-padded decimal number
# %A - Full weekday name
print(f"Full weekday: {datetime.now().strftime('%A')}")

# %B - Full month name
print(f"Full month: {datetime.now().strftime('%B')}")

# %a - Abbreviated weekday name
print(f"Abbreviated weekday: {datetime.now().strftime('%a')}")

# %b - Abbreviated month name
print(f"Abbreviated month: {datetime.now().strftime('%b')}")

# %d - Day of month
print(f"Day of month: {datetime.now().strftime('%d')}")

# %m - Month as zero-padded decimal
print(f"Month: {datetime.now().strftime('%m')}")

# %Y - Year with century
print(f"Year with century: {datetime.now().strftime('%Y')}")

# %y - Year without century
print(f"Year without century: {datetime.now().strftime('%y')}")

# %H - Hour (24-hour clock)
print(f"Hour (24-hour): {datetime.now().strftime('%H')}")

# %I - Hour (12-hour clock)
print(f"Hour (12-hour): {datetime.now().strftime('%I')}")

# %p - AM or PM
print(f"AM/PM: {datetime.now().strftime('%p')}")

# %M - Minute
print(f"Minute: {datetime.now().strftime('%M')}")

# %S - Second
print(f"Second: {datetime.now().strftime('%S')}")

# %f - Microsecond
print(f"Microsecond: {datetime.now().strftime('%f')}")

# %j - Day of year
print(f"Day of year: {datetime.now().strftime('%j')}")

# %U - Week number (Sunday as first day)
print(f"Week number (Sunday): {datetime.now().strftime('%U')}")

# %W - Week number (Monday as first day)
print(f"Week number (Monday): {datetime.now().strftime('%W')}")

print(f"Today's date: {datetime.now().strftime('%Y-%m-%d')}")
print(f"date time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S or %Y-%m-%d %I:%M:%S %p or %Y-%m-%d %H:%M:%S.%f or %Y-%m-%d %H:%M:%S.%f%z or %d-%m-%y or %m-%d %H:%M:%S.%f%z or %A, %B %d, %Y or %a, %b %d, %Y or %Y-%j or %Y-%W-%w')}")

print(f"yesterday's date: {(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')}")

print(f"Next day :{(datetime.now() + timedelta(days=1)).strftime('%d-%m-%Y')}")

print(f"Today`date :{(datetime.now()).strftime('%Y-%m-%d')}")

today=datetime.now()
dobs=datetime(2004, 5, 13)
myAge=today-dobs
print(f"My Age :{myAge}")