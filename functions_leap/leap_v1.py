
# This is the version of leap with a function handling all the code
# It works but is not really reusable

def is_leap_year():
    # Input a year
    year = int(input('Enter a year'))

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

# This is required to start the program
is_leap_year()
