"""
ENPM605 - Python Applications for Robotics
Lecture 3: Python Fundamentals — Part II
Spring 2026 | University of Maryland

Section: Dictionaries
"""

# ============================================================
# Dictionary Basics
# ============================================================

# ──────────────────────────────────────────────
# 📌 Snippet 46 — Dictionary Basics
# ──────────────────────────────────────────────
# Robot configuration dictionary
robot = {
    "name": "TurtleBot3",
    "type": "mobile",
    "max_speed": 0.26,
    "sensors": ["lidar", "camera", "imu"]
}

print(robot["name"])      # TurtleBot3
print(robot["max_speed"]) # 0.26


# # ============================================================
# # Creating Dictionaries
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippets 47-50 — Ways to Create Dictionaries
# # ──────────────────────────────────────────────
# # Curly braces with key-value pairs
# d = {"name": "Alice", "age": 30}
# empty = {}

# # dict() constructor
# d = dict(name="Alice", age=30)              # Keyword arguments
# print(d)

# d = dict([("name", "Alice"), ("age", 30)])  # List of tuples
# print(d)

# d = dict({"name": "Alice"}, age=30)         # Mixed
# print(d)

# # Dictionary comprehension
# squares = {x: x**2 for x in range(5)}
# print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# # dict.fromkeys()
# keys = ["a", "b", "c"]
# d = dict.fromkeys(keys, 0)
# print(d)  # {'a': 0, 'b': 0, 'c': 0}


# # ============================================================
# # Accessing and Modifying Dictionaries
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 51
# # ──────────────────────────────────────────────
# robot = {"name": "UR5", "joints": 6}

# # ──────────────────────────────────────────────
# # Accessing Dictionary Values
# # ──────────────────────────────────────────────
# print(robot["name"])         # UR5
# print(robot.get("speed"))    # None (no KeyError!)
# print(robot.get("speed", 0)) # 0 (default value)

# # Check if key exists
# if "name" in robot:
#     print(f"Robot name: {robot['name']}")


# # ──────────────────────────────────────────────
# # Adding/Modifying
# # ──────────────────────────────────────────────
# robot = {"name": "UR5", "joints": 6}

# # Adding/modifying items
# robot["speed"] = 1.0         # Add new key
# robot["joints"] = 7          # Modify existing
# print(robot)

# # ──────────────────────────────────────────────
# # Removing Items
# # ──────────────────────────────────────────────
# del robot["speed"]           # Remove key (KeyError if missing)
# print(robot)

# robot["payload"] = 5
# value = robot.pop("payload")  # Remove and return value
# print(f"Removed payload: {value}")
# print(robot)

# # ──────────────────────────────────────────────
# # Clear all items
# # ──────────────────────────────────────────────
# robot_copy = {"a": 1, "b": 2}
# robot_copy.clear()
# print(robot_copy)  # {}


# # ============================================================
# # Iterating Over Dictionaries
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 52 — Iterating Over Dictionaries
# # ──────────────────────────────────────────────
# robot = {"name": "TurtleBot", "type": "mobile", "speed": 0.26}

# # Iterate over keys (default)
# print("Keys:")
# for key in robot:
#     print(f"  {key}")

# # Iterate over values
# print("\nValues:")
# for value in robot.values():
#     print(f"  {value}")

# # Iterate over key-value pairs
# print("\nKey-Value pairs:")
# for key, value in robot.items():
#     print(f"  {key}: {value}")


# # ──────────────────────────────────────────────
# # 📌 Snippet 38 — Dictionary View Objects
# # ──────────────────────────────────────────────
# robot = {"name": "TurtleBot", "type": "mobile"}

# # View objects are dynamic
# keys = robot.keys()
# print(keys)  # dict_keys(['name', 'type'])

# robot["speed"] = 0.26
# print(keys)  # dict_keys(['name', 'type', 'speed']) - updated!


# # ──────────────────────────────────────────────
# # 📌 Snippet 39 — Dictionary Comprehensions
# # ──────────────────────────────────────────────
# # Basic comprehension
# squares = {x: x**2 for x in range(5)}
# print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# # With condition
# even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# # Transforming keys and values
# words = ["apple", "banana", "cherry"]
# word_lengths = {word: len(word) for word in words}
# print(word_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}

# # Inverting a dictionary
# original = {"a": 1, "b": 2, "c": 3}
# inverted = {v: k for k, v in original.items()}
# print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
