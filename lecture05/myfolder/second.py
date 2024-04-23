# Full file imports
import first

tax1, total1 = first.calculate_gst_and_total(18, 100)
print(total1)
print(tax1)

# Function import from file

from first import calculate_gst_and_total

tax2, total2 = calculate_gst_and_total(18, 100)
print(total1)
print(tax1)

# function import with alias as some_name
from first import calculate_gst_and_total as some_name

some_name(18, 100)      # works same as above