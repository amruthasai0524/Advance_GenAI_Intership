# =========================================================
# Data Science Internship - Logic Building Task 1
# Author: Amrutha Reddy
# =========================================================

# =========================================================
# 1. User Login Check
# =========================================================

print("========== TASK 1 : USER LOGIN CHECK ==========")

username = "admin"
password = "1234"

input_username = input("Enter Username: ")
input_password = input("Enter Password: ")

if input_username == username and input_password == password:
    print("Login Successful")
else:
    print("Invalid Credentials")


# =========================================================
# 2. Pass / Fail Analyzer
# =========================================================

print("\n========== TASK 2 : PASS / FAIL ANALYZER ==========")

marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Total Students Passed :", pass_count)
print("Total Students Failed :", fail_count)


# =========================================================
# 3. Simple Data Cleaner
# =========================================================

print("\n========== TASK 3 : SIMPLE DATA CLEANER ==========")

names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned_name = name.strip().lower()
    cleaned_names.append(cleaned_name)

print("Cleaned Names List:")
print(cleaned_names)


# =========================================================
# 4. Message Length Analyzer
# =========================================================

print("\n========== TASK 4 : MESSAGE LENGTH ANALYZER ==========")

messages = ["Hi", "Welcome to the platform", "OK"]

for message in messages:
    length = len(message)

    print(f"Message: '{message}'")
    print("Length:", length)

    if length > 10:
        print("Flag: Long Message")

    print()


# =========================================================
# 5. Error Message Detector
# =========================================================

print("========== TASK 5 : ERROR MESSAGE DETECTOR ==========")

logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

for log in logs:
    if log == "ERROR":
        error_count += 1

print("Total ERROR Entries:", error_count)

print("\n========== PROJECT COMPLETED SUCCESSFULLY ==========")
