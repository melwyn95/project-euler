def is_leap_year(n):
    return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)

# We know this because 1st Jan 1990 was a Monday
known_sunday = (7, 1, 1900)

def days_in_month(m, is_leap):
    if m == 1: return 31
    elif m == 2: return 29 if is_leap else 28
    elif m == 3: return 31
    elif m == 4: return 30
    elif m == 5: return 31
    elif m == 6: return 30
    elif m == 7: return 31
    elif m == 8: return 31
    elif m == 9: return 30
    elif m == 10: return 31
    elif m == 11: return 30
    elif m == 12: return 31

def next_sunday(date):
    day, month, year = date
    day += 7
    dim = days_in_month(month, is_leap_year(year))
    if day > dim: 
        day = day - dim
        month += 1
    if month > 12: 
        month = 1
        year += 1
    return (day, month, year)

def is_done(date):
    day, month, year = date
    return day >= 31 and month >= 12 and year >= 2000

sunday = (6, 1, 1901)

count = 0

while not is_done(sunday):
    sunday = next_sunday(sunday)
    if sunday[0] == 1: count += 1

print(count)
