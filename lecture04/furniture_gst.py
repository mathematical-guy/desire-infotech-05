

values = input("Enter prices:  ")


print(values)
print(values.split(' '))
prices = values.split(' ')
# price * 18 / 100

for price in prices:
    price_float = float(price)
    gst = price_float * 18/100
    print(price_float, " ===> ", gst)
