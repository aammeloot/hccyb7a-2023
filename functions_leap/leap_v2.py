
# This is the version of leap taking the year as a parameter
# It handles the display

def is_leap_year(year):
    # Ensure it's part of the Gregorian calendar
    if year > 1582:
        # Decision tree below
        if year%400 == 0:
            print("leap year")
        elif year%100 == 0:
            print("common year")
        elif year%4 == 0:
            print("leap year")
        else:
            print("common year")
    else:
        print("The Gregorian calendar starts in 1582.")


# input a year
year_choice = int(input('Enter a year'))

# This is required to start the program
is_leap_year(year_choice)
