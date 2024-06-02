
def myfunc1(x):
    return 3 + x

myf1 = myfunc1      # changes name of myfunc1 to myf1


# lambda x, y, z: return1, return2
myfunc2 = lambda x:3 + x



print(myfunc1(5))
print(myf1(5))
print(myfunc2(5))

def check_greater_than_10(x):
    return x > 10

zzzz = lambda x: x > 10

y = list(filter(check_greater_than_10, [4, -30, 23, 90, 2]))

print(y)
# map
# reduce