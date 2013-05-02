#!python

def count_days(month, year):
    if month in [3, 5, 8, 10]:
        return 30
    elif month == 1:
        if year%400 == 0 or year%4 != 0:
            return 28
        else:
            return 29
    else:
        return 31

        
count = 0
weekday = 0 #0 is Monday, 6 is Sunday
day = 0
month = 0
year = 1900
while(year <= 2000):
    #print "Weekday:", weekday, "  DOM:", day, "  Month:", month, "  Year:", year
    if year >= 1901:
        if weekday == 6 and day == 0:
            # Its a Sunday and the first of the month
            count += 1
    weekday = (weekday+1)%7
    day = (day+1)%count_days(month,year)
    if day == 0:
        month = (month+1)%12
    if month == 0 and day == 0:
        year += 1
        
print "Sudays:", count