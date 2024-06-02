import string


# mylist = list(range(350, 1251))
# mylist = []
# for index in range(1, 21):
#     result = index * 5
#     if result % 10 == 0:
#         mylist.append(result)

# print(mylist)

mylist = [index*5 if index*5 % 10 != 0 else False for index in range(1, 21) ]
print(mylist)


# START = 65
# characters = [chr(value) for value in range(START, START + 26)]
# print(characters)