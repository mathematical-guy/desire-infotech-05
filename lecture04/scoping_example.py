"""
Scope of variable
Variable defined inside a function, is not accessible
out the function. When function execution is completed,
the variable is destroyed from the memory and is not longer available


Types of Scope:
  - Local  Scope    (Would be accessible in only one function)
  - Global Scope    (Would be accessible in all functions)
"""



def addition():
    a = 80                      # Local Variable 
    print(a + b)        
    return [a + b, "mohit"]     # Returning multiple values     


def subtraction():
    a = 30
    z = addition()
    print(a - b)
    print(z)


b = 20
subtraction()
print(b)



mylist = [2, False]
print(mylist.append())