# For loop = determine how many times you repeat

for n in range(10):
    print("Hello")

    
# You can keep track with the variable (counter)
for counter in range(10):
    print("Hi", counter)

# You can also get users to determine the repetitions
amount = int(input("Enter a number"))

for counter in range(amount):
    print("This is display number:", counter + 1)


# You change the start, end, and step
for counter in range(10, 0, -2):
    print(counter)

