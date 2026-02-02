"""
ENPM605 - Python Applications for Robotics
Lecture 2: Python Fundamentals — Part I
Spring 2026 | University of Maryland

Section: Exercises
"""

# ============================================================
# Exercise 1: Operators (5 min)
# ============================================================

# ──────────────────────────────────────────────
# 📌 Snippet 14 — Exercise 1: Operators
# ──────────────────────────────────────────────
# Predict the output of each expression BEFORE running the code.

# Arithmetic
print(17 // 5)
print(17 % 5)
print(2 ** 0.5)
print(-7 // 2)

# Logical with non-boolean values
print(0 or "default")
print("hello" and "world")
print(not [])

# Chained comparison
x = 15
print(10 < x < 20)
print(10 < x > 20)


# # ============================================================
# # Exercise 2: Strings (10 min)
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 30 — Exercise 2, Part A: Predict the outputs
# # ──────────────────────────────────────────────
# text = "Learn Python, be happy!"
# print(text[6:12])
# print(text[-6:])
# print(text[::3])


# # ──────────────────────────────────────────────
# # 📌 Snippet 31 — Exercise 2, Part B: Slicing tasks
# # ──────────────────────────────────────────────
# quote = "Learn Python, be happy!"

# # Task 1: Extract "Python" using only positive indices
# # task1 = ??

# # Task 2: Extract "Python" using only negative indices
# # task2 = ??

# # Task 3: Reverse "Python" to get "nohtyP" using slicing
# # task3 = ??

# # Task 4: Reverse the entire string
# # task4 = ??


# # ──────────────────────────────────────────────
# # 📌 Snippet 32 — Exercise 2, Part C: Second half
# # ──────────────────────────────────────────────
# text = "HelloWorld"
# # second_half = ??
# # print(second_half)  # Expected: World


# # ============================================================
# # Exercise 3: Control Flow (10 min)
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 38 — Exercise 3, Part A: Battery classifier
# # ──────────────────────────────────────────────
# battery_level = 45  # Change this value to test

# # If battery_level >= 80: print "Battery: Full"
# # If 50 <= battery_level < 80: print "Battery: Moderate"
# # If 20 <= battery_level < 50: print "Battery: Low"
# # If battery_level < 20: print "Battery: Critical — return to base!"


# # ──────────────────────────────────────────────
# # 📌 Snippet 39 — Exercise 3, Part B: Leap year checker
# # ──────────────────────────────────────────────
# year = 2024

# # A year is a leap year if:
# # - Divisible by 4 AND not divisible by 100
# # - OR divisible by 400
# # Print "Leap year" or "Not a leap year"
# # Hint: Use % (modulus) to check divisibility. year % 4 == 0 means divisible by 4.


# # ============================================================
# # Exercise 4: Robot Status Monitor (15 min)
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 40 — Exercise 4: Robot Status Monitor
# # ──────────────────────────────────────────────

# # Robot parameters (add type hints to all variables)
# robot_name = "Waffle_01"
# battery = 65
# speed = 0.8
# status_log = "IDLE:MOVING:CHARGING:MOVING:IDLE"

# # 1. Use an f-string to print: "Robot Waffle_01 | Battery: 65%"

# # 2. Classify battery level using if/elif/else:
# #    >= 80: "OK", 50-79: "LOW", 20-49: "WARNING", < 20: "CRITICAL"

# # 3. Use string methods to:
# #    a) Count how many times "MOVING" appears in status_log
# #    b) Split status_log by ":" into a list
# #    c) Check if the last status is "IDLE"

# # 4. Use slicing to extract the first status entry from status_log

# # 5. Create a formatted status message:
# #    "Waffle_01 | Battery: LOW | Speed: 0.80 m/s | States: 5"