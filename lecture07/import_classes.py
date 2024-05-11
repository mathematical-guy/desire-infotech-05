
class Switch:
    color = "White"
    poles = 2


# following code will only run when this file is executed
# it will run automatically (outside main), if anything is imported from this file
first_switch = Switch()
second_switch = Switch()

if __name__ == "__main__":
    # following code will only run when this file is executed
    # it will not run, if anything is imported from this file
    print('*'*10)
    print("Yeh wala first hai",first_switch, type(first_switch))
    print("Yeh wala second hai", second_switch, type(second_switch))
    print('*'*10)