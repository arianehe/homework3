cents = int(input("Input your cents (an integer greater than 0 no more than 100): "))

quarters = cents // 25
remaining = cents % 25

dimes = remaining // 10
remaining = remaining % 10

nickels = remaining // 5
remaining = remaining % 5

pennies = remaining

print("Your change is:")
if quarters != 0:
    print( quarters, 'quarters')
if dimes != 0:
    print( dimes, 'dimes')
if nickels != 0:
    print( nickels, 'nickels')
if pennies != 0:
    print( pennies, 'pennies')