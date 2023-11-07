
# This is more modular approach:
# Function taking a year and checking if it is leap (returning Boolean or Nothing)

def is_gregorian_year(year):
    return year > 1582

def is_leap_year(year):
    # Decision tree below
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False


# The main program
def main():
    # Use the function with I/O
    # input a year
    year_choice = int(input('Enter a year'))

    # If the year is Gregorian, check if leap
    if is_gregorian_year(year_choice):
        # Check leap
        if is_leap_year(year_choice):
            print("This is a leap year")
        else:
            print("This is a common year")
    else:
        print("The year not a valid Gregorian calendar year")

'''
    # Use function in a different way (batch process)
    years = [1999, 2004, 1900]
    leaps = []

    for y in years:
        leaps.append(is_leap_year(y))

    print(leaps)
'''


# Ensure main() only runs if this is not loaded as a module
# For another program
if __name__ == "__main__":
    # Start the main program
    main()

