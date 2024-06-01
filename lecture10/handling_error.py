

# a = 4 / 0       # ZeroDivisionError: division by zero
# a = int("mohit")    # ValueError: invalid literal for int() with base 10: 'mohit'

try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    #erthjkl;'
    #erthjkl;'
    #erthjkl;'
    #erthjkl;'
    print(a/b)
    print(a/b)
    print(a/b)
    print(a/b)

except ZeroDivisionError as x:
    print("Zero nahi daalna chahiye, galat baat hai", type(x))
except ValueError:
    print("Please enter a valid number")

except Exception as err:
    print("Kuch to gadbad hai", err)

else:
    print("aksdhsdoipiuyt")
    print("oiuytfghjkl;")
    print("aksdhsdoipiuyt")