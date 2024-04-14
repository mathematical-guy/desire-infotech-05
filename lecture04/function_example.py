
"""
function syntax:

def function_ka_name():
    functionality ka statement 1
    functionality ka statement 2
    functionality ka statement 3

"""
print("Ye function ke upar wali line hai")
x = 3
def greeting():
    print("Hello")
    print("Good morning")
    print("Kaise ho")

def add_numbers():
    a = 30
    b = 90
    print("Pehle number hai ", a)
    print("Dusra number hai ", b)
    c = a + b
    print("Result hai: ", c)


def calculate_rectangle_area(length, breadth):
    area = length * breadth
    print(area)

def calculate_cube_of_number(number):
    cube = number * number * number
    return cube         # Returning a value

def calculate_love_percentage(name):
    crush_ki_list = ["kabootar", "maskali", "katrina", 'kriti']
    dushman_ki_list = ["devdas", "abc"]

    if name in crush_ki_list:
        print("Your love percentage is: ", 100)
    elif name in dushman_ki_list:
        print("Your love percentage is: ", 0)
    else:
        print("Your love percentage is: ", 50)



calculate_rectangle_area(10)
calculate_love_percentage("katrina")