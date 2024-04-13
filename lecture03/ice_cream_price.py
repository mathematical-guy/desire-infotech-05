

FLAVOURS = ["chocolate", "strawberry", "pineapple", "rajbhog"]

print("Available Flavours are: ")
print(FLAVOURS)
user_flavour = input("Choose a flavour")

if user_flavour == "chocolate":
    print("You have selected chocolate and your price is ", 80) 
elif user_flavour == "strawberry":
    print("You have selected strawberry and your price is ",  90)
elif user_flavour == "pineapple":
    print("You have selected pineapple and your price is ",  40)
elif user_flavour == "rajbhog":
    print("You have selected rajbhog and your price is ", 120)
else:
    print("Wrong Input, Please enter a valid input")
