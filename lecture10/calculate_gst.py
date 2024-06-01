GST = 0.18
# tax = 0
price = int(input("Enter Price: "))
if price < 0:
    print("Invalid value")
    # exit()
    raise Exception("Kuch to gadbad hhai Daya.")
else:
    tax = price * GST
    print("Your tax is ", tax)


print("TAX is: ", tax)