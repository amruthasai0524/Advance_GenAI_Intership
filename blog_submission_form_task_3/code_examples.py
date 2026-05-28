# =========================================================
# Python Dictionaries Complete Examples
# =========================================================

# Creating Dictionary
student = {
    "name": "Amrutha",
    "age": 21,
    "course": "Data Science"
}

print(student)

# Accessing Values
print(student["name"])

# Adding Values
student["city"] = "Hyderabad"
print(student)

# Updating Values
student["age"] = 22
print(student)

# Removing Values
del student["city"]
print(student)

# Looping Through Dictionary
for key, value in student.items():
    print(key, ":", value)

# Dictionary Methods
print(student.keys())
print(student.values())
print(student.items())