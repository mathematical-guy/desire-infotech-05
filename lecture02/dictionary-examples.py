mydictionary = {
    "roll_no": 31,
    "name": "Mohit",
    "address": "Ahmedabad",
    "father_name": "XYZ",
    "subjects": ["XYZ", "Maths", "Hindi"],
    "marks": {
        "hindi": 33,
        "gujarati": 80,
        "maths": 99,
    }
}

print(mydictionary)
print(mydictionary["address"])
mydictionary["roll_no"] = 19

print(mydictionary)


students = [
    {"name": "ABC", 'roll_no': 33},
    {"name": "ADC", 'roll_no': 31},
    {"name": "XYZ", 'roll_no': 32},
]
print('**********************\n')
# print(students)
print(students[0]["name"], students[0]["roll_no"])
print(students[1]["name"], students[1]["roll_no"])
print(students[2]["name"], students[2]["roll_no"])
# print(students)
print(mydictionary["address"])
print(mydictionary.get("addressiuytreadfy"))