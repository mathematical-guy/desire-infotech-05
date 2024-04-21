"""
Consider a following function which calculates x to the power y

X^Y = X*X*X*... (Y times)
4^3 = 64
3^5 = 243

def calculate_power(x, y):
    return x**y


1) When function is called passed arguments must follow:
   a. No of arguments (i.e both X and Y should be passed and not more or less)
   b. Data types of the Arguments (both should be number int/float)
   c. Order of arguments (X^Y and Y^X are two different results)

2) When function is called return values must follow:
   a. No of returned values
   b. Data types of the returned value(s)
   c. Order of returned values 

To prevent point a packing operators can be used (using * or **)
To prevent point b type hinting while defining the function
To prevent point c keyword arguments can be used
""" 

def calculate_power1(x, y):
    return x ** y

# Here what datatype is requried to sent to function is not clear
print(calculate_power1(31, 3))  
print(calculate_power1("a", False))

# -------------------------- Function with Type Hinting -------------------

def calculate_power2(
        x: int,     # Type hinting denotes x is integer 
        y: int,     # Type hinting denotes y is integer 
    ) -> int:       # Type hinting denoting returned value is integer
    
    return x ** y  


# Here no of arguments are different from the argument mention in function
print(calculate_power2(5))
print(calculate_power2(5, 2, 3, 15, -23, False))

# -------------------------- Function with handling no of arguments -------------------

# Note: args would be tuple for positional arguments
# and kwargs would be a dictionary for keyword arguments

def calculate_power3(x: int, y: int, *args, **kwargs) -> int:       # Type hinting denoting returned value is integer
    return x ** y  

# These two will give same result irrespective of the order of arguments
print("**"*20)
print(calculate_power3(y=3, x=2))
print(calculate_power3(x=2, y=3))
print(calculate_power3(y=9, z=12, x=4, e=-3))
