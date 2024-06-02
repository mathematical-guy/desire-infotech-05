import time

def calculate_time(function):
    start = time.time()
    function()
    end = time.time()
    print(abs(end - start))

def append_functionality():
    numbers = []
    for i in range(1, 1000001):
        numbers.append(i*4 + 5)

    print(len(numbers))

def list_comprehension():
    new_numbers = [x*4 + 5 for x in range(1, 1000001)]
    print(len(new_numbers))

calculate_time(append_functionality)
calculate_time(list_comprehension)