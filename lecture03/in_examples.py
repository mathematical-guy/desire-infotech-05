
name = "ABCDE"

# Syntax: element in collection
# collection can be list/tuple/dictionary/set/string

print("A" in name)      # True
print("a" in name)      # False
print("X" in name)      # False
print("x" in name)      # False

print("a" not in name)      # True
print("A" not in name)      # False
print("X" not in name)      # True
print("x" not in name)      # True
