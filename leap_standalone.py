

year = int(input('Enter a year'))

if year > 1582:
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
