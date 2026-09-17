import math

date = str(input("Enter the date, sepreted by /s: "))

data = date.split("/")

def calculate(month, day, year):
    # Zeller's Congruence rule: January and February are months 13 and 14 of the PREVIOUS year
    if month < 3:
        month += 12
        year -= 1

    # Calculate the day index (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)
    # Changed from '7 % sum' to 'sum % 7'
    day_index = (day + math.floor((13 * (month + 1)) / 5) + year + 
                 math.floor(year / 4) - math.floor(year / 100) + 
                 math.floor(year / 400)) % 7

    days_of_week = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday"
    }
                 
    return days_of_week.get(day_index)

print(calculate(int(data[0]), int(data[1]), int(data[2])))