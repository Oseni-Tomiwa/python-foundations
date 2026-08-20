# while loops

# A for loop is for a known collection or fixed sequence.

# for topic in topics:
#     print(topic)

# A while loop repeats while a condition remains true.

# completed_hours = 0
# target_hours = 5
# while completed_hours < target_hours:
#     completed_hours += 1
#     print(f"Study hour logged: {completed_hours}")

# Output:

# Study hour logged: 1
# Study hour logged: 2
# Study hour logged: 3
# Study hour logged: 4
# Study hour logged: 5

# This line is crucial:

# completed_hours += 1

# It means:

# completed_hours = completed_hours + 1

# Without it, completed_hours stays at 0, so the condition stays true forever—an infinite loop.

# while completed_hours < target_hours:
#     print("Still studying")

# If that happens, stop the running program with:

# Control + C

# Use while when you don’t know exactly how many repetitions are needed—for example, retrying a failed message delivery or waiting for a background AI job to finish. For a known list of documents, use for.


target_hours = int(input("What is your study target today? "))

if target_hours <= 0:
    print("Study target must be greater than zero.")
else:
    completed_hours = 0

    while completed_hours < target_hours:
        completed_hours += 1
        print(f"Hour {completed_hours} logged.")

    print("Daily study target completed.")