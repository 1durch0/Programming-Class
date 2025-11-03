login_attempts = [
    ("alice", True),
    ("bob", False),
    ("bob", False),
    ("bob", False),
    ("alice", False),
    ("jonas", False),
    ("jonas", False),
    ("bob", False),
    ("bob", False),
    ("alice", False),
    ("jonas", True),
]
# Base dictionary
attempt_counts = {}

# creating inner dictionaries for the outer ones to store the Booleans -> recursive structure
for name, result in login_attempts:
    if name not in attempt_counts:
        attempt_counts[name] = {"True": 0, "False": 0}
    if result:
        attempt_counts[name]["True"] += 1
    else:
        attempt_counts[name]["False"] += 1

# Display results and check for alerts
for name in attempt_counts:
    true_count = attempt_counts[name]["True"]
    false_count = attempt_counts[name]["False"]
    print(f"{name}: {true_count} True, {false_count} False")

    # Alert if more than 3 failed attempts
    if false_count > 3:
        print(f"ALERT: {name} has {false_count} failed login attempts!")

