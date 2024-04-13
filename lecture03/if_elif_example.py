age = 39
DRIVE_AGE = 18

MIN_AGE = 0
MAX_AGE = 100

if age < MIN_AGE or age > 100:
    print("Invalid age")
elif age >= DRIVE_AGE:
     print("You can drive")
else:
    print("You cannot drive")
