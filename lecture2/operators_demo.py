"""
ENPM605 - Python Applications for Robotics
Lecture 2: Python Fundamentals — Part I
Spring 2026 | University of Maryland

Section: Operators
"""

# ============================================================
# Arithmetic Operators
# ============================================================

# ──────────────────────────────────────────────
# 📌 Snippet 9 — Arithmetic Operators
# ──────────────────────────────────────────────
# Floor division always rounds toward negative infinity
print(10 // 3)    # 3
print(10 // -3)   # -4 (not -3!)

# Augmented assignment operators
x = 10
x += 5   # x = x + 5 -> 15
x *= 2   # x = x * 2 -> 30
print(f"x = {x}")


# # ============================================================
# # Relational (Comparison) Operators
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 10 — Chained Comparisons
# # ──────────────────────────────────────────────
# # Python supports chained comparisons
# x = 5
# print(1 < x < 10)   # True (equivalent to 1 < x and x < 10)
# print(1 < x > 3)    # True


# # ============================================================
# # Logical Operators
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 11 — Logical Operators
# # ──────────────────────────────────────────────
# # Short-circuit evaluation
# x = 5
# print(x > 0 and x < 10)    # True
# print(x > 10 or x == 5)    # True
# print(not (x == 5))        # False

# # Logical operators with non-boolean values
# # and: returns first falsy, or last value if all truthy
# print("hello" and 0)          # 0 ("hello" is truthy, so check 0 -> falsy)
# print("hello" and "world")    # "world" (both truthy, return last)

# # or: returns first truthy, or last value if all falsy
# print("hello" or 0)           # "hello" (truthy, stop immediately)
# print(0 or "default")         # "default" (0 is falsy, check next)

# # not: always returns a bool
# print(not "")                  # True (empty string is falsy)
# print(not "hello")             # False (non-empty string is truthy)


# # ============================================================
# # Membership and Identity Operators
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 12 — Membership Operators
# # ──────────────────────────────────────────────
# x = "hello"
# print("h" in x)      # True
# print("he" in x)     # True
# print("O" in x)      # False
# print("z" not in x)  # True


# # ──────────────────────────────────────────────
# # 📌 Snippet 13 — Identity Operators
# # ──────────────────────────────────────────────
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print(a == b)   # True (same values)
# print(a is b)   # False (different objects)
# print(a is c)   # True (same object)