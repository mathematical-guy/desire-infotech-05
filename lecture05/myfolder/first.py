
# This is general function which can be used anywhere
def calculate_gst_and_total(gst, price):
    tax = gst * price / 100
    total = tax + price

    return tax, total
