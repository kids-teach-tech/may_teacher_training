height_feet = int(input("How tall are you in feet? "))
height_inches = int(input("How many additional inches? "))

if height_feet == 5:
    if height_inches == 11:
        height_feet = 6
        height_inches = 0

if height_inches == 0:
    print("You are actually " + str(height_feet) + " feet tall!")
else:
    print("You are actually " + str(height_feet) + " feet and " + str(height_inches) + " inches tall!")