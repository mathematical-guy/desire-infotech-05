import time

def calculate_time(v):
    def inner_function():
        start = time.time()
        v()
        end = time.time()
        print(abs(end - start))
    
    return inner_function

@calculate_time
def append_functionality():
    numbers = []
    for i in range(1, 1000001):
        numbers.append(i*4 + 5)

    print(len(numbers))

@calculate_time
def list_comprehension():
    new_numbers = [x*4 + 5 for x in range(1, 1000001)]
    print(len(new_numbers))

# print(outer_function(append_functionality)())
# print(outer_function(list_comprehension)())


print(append_functionality())
print(list_comprehension())